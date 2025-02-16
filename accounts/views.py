from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.contrib.auth.models import User
from validate_email import validate_email
from django.utils.http import urlsafe_base64_decode
from .utils import token_generator,send_activation_email,send_reset_password_link
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
import logging
from .forms import ContactForm
from .models import ContactMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile


logger = logging.getLogger(__name__)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the message to the database
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message'],
            )
            messages.success(request, "Thank you for contacting us! We'll get back to you soon.")
            return redirect('contact')
        else:
            messages.error(request, "Please fill out all required fields correctly.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


class RegistrationView(View):
    def get(self,request):
        return render(request,'accounts/register.html')
    
    def post(self,request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        context = {
            'fieldsValues': request.POST
        }

        # Check if passwords match
        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'accounts/register.html', context)
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return render(request, 'accounts/register.html', context)
        
        if not validate_email(email):
            messages.error(request, 'Invalid email format.')
            return render(request, 'accounts/register.html', context)

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return render(request, 'accounts/register.html', context)
        
        # Validate password using Django's built-in password validation
        try:
            validate_password(password, user=User)
        except ValidationError as e:
            for message in e.messages:
                messages.error(request, message)
            return render(request, 'accounts/register.html', context)

        # Use a transaction to ensure atomicity
        try:
            with transaction.atomic():
                # Create the user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.is_active = False  # User needs to activate their account via email
                user.save()

                # Send activation email
                is_sent = send_activation_email(request, user)
                if not is_sent:
                    # If email fails, raise an exception to trigger a rollback
                    raise Exception("Failed to send activation email.")

                # If everything is successful
                messages.success(request, 'Account successfully created. Please check your email to activate it.')
                return redirect('login')  # Redirect to login page after successful registration

        except Exception as e:
            # Log the error and notify the user
            logger.error(f"Error during registration: {e}")
            messages.error(request, 'Failed to complete registration. Please try again.')
            return render(request, 'accounts/register.html', context)

class VerificationView(View):
    def get(self,request,uidb64,token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not token_generator.check_token(user,token):
                messages.error(request, "User already activated.") 
                return redirect('login')
            
            user.is_active = True
            user.save()
            messages.success(request,"Account Successfully activated.")
            return redirect('login')

        except Exception as e:
            pass

        return redirect('login')
    
class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth.login(request, user)
                    messages.success(request, f"Welcome, {user.username}. You are now logged in.")
                    return redirect('home')
            else:
                if User.objects.filter(username=username).exists() and User.objects.get(username=username).is_active:
                    messages.error(request, "Invalid credentials. Please try again.")  
                elif not User.objects.filter(username=username).exists():
                    messages.error(request, "Invalid credentials. Please try again.")      
                else:
                    messages.error(request, "Your account is not active. Please check your email for activation instructions.")
        else : 
            messages.error(request, "Please fill in all fields.")
        return render(request, 'accounts/login.html')

class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request,"You have been logged out")
        return redirect('login')
    
class ResetPasswordView(View):
    def get(self, request):
        return render(request,'accounts/reset_password.html')
    
    def post(self, request):

        email = request.POST['email']
        if not validate_email(email):
            messages.error(request, "Please enter valid email")
            return render(request,'accounts/reset_password.html')
        
        user = User.objects.filter(email=email)

        if user:
            send_reset_password_link(request,user[0])
        
        messages.success(request,"We have sent you an email to reset password")
        
        return render(request,'accounts/reset_password.html')
    
class CompletePasswordReset(View):
    def get(self,request,uidb64,token):
        
        context = {
            'uidb64': uidb64,
            'token': token
        }

        try:

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            if not PasswordResetTokenGenerator.check_token(PasswordResetTokenGenerator(),user,token):
                messages.info(request,"Link is invalid , Please request new one")
                return render(request,'accounts/reset_password.html')
        
        except:
            messages.info(request,"Something went wrong, try again")
            return render(request,'accounts/set_new_password.html',context)
        
    
        return render(request,'accounts/set_new_password.html',context)
    
    def post(self,request,uidb64,token):
        context = {
            'uidb64': uidb64,
            'token': token
        }

        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            messages.error(request,"Passwords do not match")
            return render(request,'accounts/set_new_password.html',context)
        
        # Validate passwords using Django's built-in password validation
        try:
            validate_password(password, user=User)
        except ValidationError as e:
            print(e)
            for message in e.messages:
                messages.error(request,message)
            return render(request, 'accounts/set_new_password.html', context)

        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            user.set_password(password)
            user.save()
            messages.success(request,"Password reset succesfully")
            return redirect('login')
        except Exception :
            messages.info(request,"Something went wrong, try again")
            return render(request,'accounts/set_new_password.html',context)

        #return render(request,'accounts/set_new_password.html',context)
    
@login_required
def profile(request):
    """Display and update the user's profile."""
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        # Update the profile with the submitted data
        profile.phone = request.POST.get('phone', profile.phone)
        profile.address = request.POST.get('address', profile.address)
        profile.save()
        return redirect('profile')  # Redirect to the profile page after saving
    
    return render(request, 'accounts/profile.html', {
        'profile': profile
    })

@login_required
def profile_updated(request):
    return render(request, 'accounts/profile_updated.html')
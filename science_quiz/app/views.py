from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User  # Import User model
from django.contrib import messages
from django.http import JsonResponse
from .models import Profile, QuizAttempt
from .forms import UserUpdateForm, ProfileUpdateForm

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        # Check if username already exists
        username = request.POST.get('username')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username is already taken. Please choose another.')
            return render(request, 'register.html', {'form': form})

        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

@login_required
def profile(request):
    """
    Display user profile and quiz history.
    """
    # Ensure user has a profile
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile_updated')  # Redirect to confirmation page
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    # Fetch user's quiz attempts sorted by latest first
    quiz_attempts = QuizAttempt.objects.filter(user=request.user).order_by('-timestamp')

    return render(request, 'profile.html', {
        'u_form': u_form, 
        'p_form': p_form, 
        'quiz_attempts': quiz_attempts
    })

def profile_updated(request):
    """
    Display confirmation message after profile update.
    """
    return render(request, 'profile_updated.html', {'message': 'Your profile has been updated successfully!'})

@login_required
def save_quiz_attempt(request):
    """
    Save quiz attempt to database for registered users.
    """
    if request.method == "POST":
        user = request.user
        question_text = request.POST.get("question_text")
        selected_answer = request.POST.get("selected_answer")
        correct_answer = request.POST.get("correct_answer")

        # Ensure required fields are present
        if not question_text or not selected_answer or not correct_answer:
            return JsonResponse({"status": "error", "message": "Missing quiz data"}, status=400)

        is_correct = selected_answer == correct_answer  # Check if the user got it right

        # Save the quiz attempt
        QuizAttempt.objects.create(
            user=user,
            question_text=question_text,
            selected_answer=selected_answer,
            correct_answer=correct_answer,
            is_correct=is_correct
        )

        return JsonResponse({"status": "success", "is_correct": is_correct})

    return JsonResponse({"status": "error"}, status=400)

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage
from email.mime.text import MIMEText
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from six import text_type
import json
import environ
import requests
from django.shortcuts import render

class AppTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (text_type(user.is_active)+text_type(user.pk)+text_type(timestamp))

token_generator=AppTokenGenerator()

def send_reset_password_link(request,user):
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    domain = get_current_site(request).domain
    token = PasswordResetTokenGenerator().make_token(user=user)
    link = reverse('reset-user-password',kwargs={
                    'uidb64': uidb64, 'token': token
    })

    reset_url = 'http://'+domain+link

    email_subject = "Reset Password for Revise Science"
    email_body = "Hi there , Please click the link below to reset your password \n " + reset_url
    email = EmailMessage(
        email_subject,
        email_body,
        "noreply@example.com",
        [user.email],
    )
    email.send(fail_silently=False)
    return True
    

'''
def send_activation_email(request,user):
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    domain = get_current_site(request).domain
    token = token_generator.make_token(user)
    link = reverse('activate',kwargs={
                    'uidb64': uidb64, 'token': token
    })

    activate_url = 'http://'+domain+link

    email_subject = "Verify Email Address for Expenses Tracker"
    email_body = "Hi "+ user.username+ ", Thanks for registering for an account on Expenses Tracker! Before we get started, we just need to confirm that this is you. Click in the below to verify your email address:\n" + activate_url
    email = EmailMessage(
        email_subject,
        email_body,
        "noreply@example.com",
        [user.email],
    )
    email.send(fail_silently=False)
    return True
'''

def send_activation_email(request,user):
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = token_generator.make_token(user)
    link = reverse('activate',kwargs={
                    'uidb64': uidb64, 'token': token
    })

    domain = get_current_site(request).domain

    activate_url = 'http://'+domain+link

    email_subject = "Verify Email Address for Revise Science"
    
    context = {
        "username": user.username,
        "link": activate_url
    }

    email_body = render_to_string('accounts/confirm_email.html', context)

    email = EmailMessage(
        subject=email_subject,
        from_email="mahdibazoka2002@gmail.com",
        to=[user.email]
    )
    mime_text = MIMEText(email_body, 'html')
    email.attach(mime_text)
    email.send(fail_silently=False)

    return True

    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    token = PasswordResetTokenGenerator().make_token(user=user)
    link = reverse('reset-user-password',kwargs={
                    'uidb64': uidb64, 'token': token
    })

    WP_url= "https://live.waypointapi.com/v1/email_messages"

    headers = {
        "Content-Type" : "application/json"
    }
    auth = (API_KEY_USERNAME, API_KEY_PASSWORD)

    data = {
        "templateId": "wptemplate_V6WYpn2cVGU3rHz8",
        "to":user.email,
        "variables":{
            "username":user.username,
            "link":link
        }
    }

    response = requests.post(WP_url,headers=headers,auth=auth,data=json.dumps(data))
    return True
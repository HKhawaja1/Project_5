from django.urls import path
from . import views
from .views import RegistrationView,VerificationView,LoginView,LogoutView,ResetPasswordView,CompletePasswordReset


urlpatterns = [
    # Authentication Routes
    path('register/',RegistrationView.as_view(),name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),

    path('profile/', views.profile, name='profile'),
    path('profile-updated/', views.profile_updated, name='profile_updated'),

    path('contact/', views.contact, name='contact'),

    # Password Reset Routes (Django Built-in)
    path('activate/<uidb64>/<token>',VerificationView.as_view(),name="activate"),
    path('reset-user-password/<uidb64>/<token>',CompletePasswordReset.as_view(),name="reset-user-password"),
    path('reset-password/',ResetPasswordView.as_view(),name="reset-password")
]
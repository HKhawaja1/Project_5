from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Home Page
    path('', views.home, name='home'),

    # Authentication Routes
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile-updated/', views.profile_updated, name='profile_updated'),  # ✅ Confirmation page after profile update

    # Password Reset Routes (Django Built-in)
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),
]

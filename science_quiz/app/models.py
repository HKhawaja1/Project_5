from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

# Signal to automatically create a Profile when a User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to registered users
    question_text = models.TextField()  # Store the question text
    selected_answer = models.CharField(max_length=255)  # User’s chosen answer
    correct_answer = models.CharField(max_length=255)  # The actual correct answer
    is_correct = models.BooleanField()  # True if the answer was correct, False otherwise
    timestamp = models.DateTimeField(auto_now_add=True)  # Stores attempt date & time

    def __str__(self):
        return f"{self.user.username} - {self.question_text} - {'✅' if self.is_correct else '❌'}"

from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Represents a quiz topic (e.g., Biology, Chemistry, Physics)."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    """Represents a question within a topic."""
    topic = models.ForeignKey(Topic, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    marks = models.PositiveIntegerField(default=1)  # Marks for this question

    def __str__(self):
        return self.text


class Option(models.Model):
    """Represents an option for a question."""
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)  # Whether this option is correct

    def __str__(self):
        return self.text

class QuizSession(models.Model):
    """Represents a single quiz session for a user."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_sessions')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='quiz_sessions')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.topic.name} - {self.start_time}"
    
class UserQuizAttempt(models.Model):
    """Represents a user's attempt for a specific question."""
    user = models.ForeignKey(User, related_name='quiz_attempts', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True)
    is_correct = models.BooleanField(default=False)  # Whether the attempt was correct
    marks_obtained = models.PositiveIntegerField(default=0)  # Marks obtained for this attempt
    timestamp = models.DateTimeField(auto_now_add=True)  # Track when the attempt was made
    session_id = models.CharField(max_length=100, blank=True, null=True)  # Add this field
    quiz_session = models.ForeignKey(QuizSession, on_delete=models.CASCADE, related_name='attempts', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.question.text}"

    def save(self, *args, **kwargs):
        """Calculate marks_obtained based on whether the selected option is correct."""
        if self.selected_option:
            self.is_correct = self.selected_option.is_correct
            self.marks_obtained = self.question.marks if self.is_correct else 0
        super().save(*args, **kwargs)
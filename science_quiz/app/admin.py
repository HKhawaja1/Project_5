from django.contrib import admin
from .models import Topic, Question, Option, UserQuizAttempt

class OptionInline(admin.TabularInline):
    """Inline editing for Options within the Question admin page."""
    model = Option
    extra = 1  # Number of empty forms to display


class QuestionInline(admin.TabularInline):
    """Inline editing for Questions within the Topic admin page."""
    model = Question
    extra = 1
    show_change_link = True  # Allow editing individual questions


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    inlines = [QuestionInline]  # Add questions directly from the Topic admin page


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'topic', 'marks')
    search_fields = ('text', 'topic__name')
    list_filter = ('topic',)
    inlines = [OptionInline]  # Add options directly from the Question admin page


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    search_fields = ('text', 'question__text')
    list_filter = ('question__topic', 'is_correct')


@admin.register(UserQuizAttempt)
class UserQuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'selected_option', 'is_correct', 'marks_obtained', 'timestamp')
    search_fields = ('user__username', 'question__text')
    list_filter = ('is_correct', 'question__topic', 'timestamp')
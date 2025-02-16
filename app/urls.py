from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [

    # Home Page
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('start-quiz/<int:topic_id>/', views.start_quiz, name='start_quiz'),
    path('quiz/<int:topic_id>/<int:question_id>/', views.quiz_question, name='quiz_question'),
    path('quiz-results/<int:topic_id>/', views.quiz_results, name='quiz_results'),

    path('submit-answer/<int:question_id>/', views.submit_answer, name='submit_answer'),
    path('results/<int:topic_id>/', views.quiz_results, name='quiz_results'),

    path('leaderboards/', views.all_topics, name='all_topics'),
    path('leaderboard/<int:topic_id>/', views.leaderboard, name='leaderboard'),

    # ✅ New Route: Save Quiz Attempt
    # path('save-quiz-attempt/', views.save_quiz_attempt, name='save_quiz_attempt'),
]

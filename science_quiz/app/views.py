from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Question, Option, UserQuizAttempt, QuizSession
import random
from django.db.models import Sum, Max
from django.db.models import Sum, OuterRef, Subquery

def home(request):
    # Fetch all topics
    topics = Topic.objects.all()

    # Pass the topics to the template
    context = {
        'topics': topics,
    }
    return render(request, 'index.html', context)
    
def about(request):
    return render(request, 'about.html')

@login_required
def start_quiz(request, topic_id):

    # Fetch the topic and all its questions
    topic = get_object_or_404(Topic, id=topic_id)

    # Create a new QuizSession
    quiz_session = QuizSession.objects.create(user=request.user, topic=topic)
    request.session['quiz_session_id'] = quiz_session.id  # Store session ID

    questions = list(topic.questions.all())

    # Shuffle the questions
    random.shuffle(questions)

    # Store the shuffled question IDs in the session
    request.session['shuffled_question_ids'] = [q.id for q in questions]
    request.session['current_question_index'] = 0

    # Redirect to the first question
    first_question_id = request.session['shuffled_question_ids'][0]
    return redirect('quiz_question', topic_id=topic_id, question_id=first_question_id)

@login_required
def quiz_question(request, topic_id, question_id):
    # Fetch the topic
    topic = get_object_or_404(Topic, id=topic_id)

    # Fetch the shuffled question IDs from the session
    shuffled_question_ids = request.session.get('shuffled_question_ids', [])
    current_question_index = request.session.get('current_question_index', 0)

    quiz_session_id = request.session.get('quiz_session_id')

    # Fetch the current question
    question = get_object_or_404(Question, id=question_id)

    # Calculate progress
    total_questions = len(shuffled_question_ids)
    progress = int((current_question_index / total_questions) * 100) if total_questions > 0 else 0

    # Handle form submission
    if request.method == 'POST':
        selected_option_id = request.POST.get('option')
        if selected_option_id:
            selected_option = Option.objects.get(id=selected_option_id)
            is_correct = selected_option.is_correct
            marks_obtained = question.marks if is_correct else 0

            # Fetch the QuizSession instance
            quiz_session = QuizSession.objects.get(id=quiz_session_id)

            # Save the user's attempt
            UserQuizAttempt.objects.create(
                user=request.user,
                question=question,
                selected_option=selected_option,
                is_correct=is_correct,
                marks_obtained=marks_obtained,
                quiz_session = quiz_session
            )

            # Move to the next question
            current_question_index += 1
            request.session['current_question_index'] = current_question_index

            # Redirect to the next question or results page
            if current_question_index < len(shuffled_question_ids):
                next_question_id = shuffled_question_ids[current_question_index]
                return redirect('quiz_question', topic_id=topic_id, question_id=next_question_id)
            else:
                return redirect('quiz_results', topic_id=topic_id)

    # Pass the question and options to the template
    context = {
        'topic': topic,
        'question': question,
        'current_question_index': current_question_index + 1,  # Human-readable index (1-based)
        'total_questions': total_questions,
        'progress': progress,  # Progress percentage
    }
    return render(request, 'quiz_question.html', context)

@login_required
def submit_answer(request, question_id):
    """Handle user's answer submission and save their attempt."""
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        selected_option_id = request.POST.get('option')
        selected_option = get_object_or_404(Option, id=selected_option_id)

        # Fetch the current QuizSession
        quiz_session_id = request.session.get('quiz_session_id')
        quiz_session = QuizSession.objects.get(id=quiz_session_id)

        # Save the user's attempt
        UserQuizAttempt.objects.create(
            user=request.user,
            question=question,
            selected_option=selected_option,
            quiz_session=quiz_session  # Link to the QuizSession
        )

        # Redirect to the next question or results page
        next_question = question.topic.questions.filter(id__gt=question.id).first()
        if next_question:
            return redirect('question_list', topic_id=question.topic.id)
        else:
            return redirect('quiz_results', topic_id=question.topic.id)

    return redirect('question_list', topic_id=question.topic.id)

@login_required
def quiz_results(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    quiz_session_id = request.session.get('quiz_session_id')

    # Fetch the QuizSession and its attempts
    quiz_session = QuizSession.objects.get(id=quiz_session_id)
    attempts = quiz_session.attempts.all()  # Use related_name to fetch attempts

    # Calculate total marks, correct answers, and incorrect answers
    total_marks = sum(attempt.marks_obtained for attempt in attempts)
    correct_answers = attempts.filter(is_correct=True).count()
    incorrect_answers = attempts.filter(is_correct=False).count()

    # Clear the session data
    if 'shuffled_question_ids' in request.session:
        del request.session['shuffled_question_ids']
    if 'current_question_index' in request.session:
        del request.session['current_question_index']
    if 'quiz_session_id' in request.session:
        del request.session['quiz_session_id']

    context = {
        'topic': topic,
        'attempts': attempts,
        'total_marks': total_marks,
        'correct_answers': correct_answers,
        'incorrect_answers': incorrect_answers,
    }
    return render(request, 'results.html', context)

@login_required
def all_topics(request):
    """Display a list of all topics."""
    topics = Topic.objects.all()
    return render(request, 'all_topics.html', {
        'topics': topics
    })

@login_required
def leaderboard(request, topic_id):
    """Display a leaderboard for a specific topic, showing the best total marks per user."""
    topic = get_object_or_404(Topic, id=topic_id)
    
    # Step 1: Calculate the total marks for each QuizSession
    total_marks_subquery = (
        UserQuizAttempt.objects
        .filter(quiz_session=OuterRef('pk'))  # Filter by the outer QuizSession
        .values('quiz_session')
        .annotate(total_marks=Sum('marks_obtained'))
        .values('total_marks')
    )
    
    # Step 2: Get the best total marks for each user
    leaderboard_data = (
        QuizSession.objects
        .filter(topic=topic)  # Filter by topic
        .annotate(total_marks=Subquery(total_marks_subquery))  # Add total_marks to each QuizSession
        .values('user__username')  # Group by user
        .annotate(
            best_marks=Max('total_marks')  # Get the maximum total marks for each user
        )
        .order_by('-best_marks')  # Sort by best marks in descending order
    )
    
    return render(request, 'leaderboard.html', {
        'topic': topic,
        'leaderboard': leaderboard_data
    })


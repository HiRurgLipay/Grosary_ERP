from django.shortcuts import render, redirect
from core.models import Question
from core.business.services import create_question, create_answer
from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_admin)
def add_question(request):
    if request.method == 'POST':
        question_text = request.POST.get('question_text')
        create_question(question_text)
        return redirect('admin_panel')
    else:
        questions = Question.objects.all()
        return render(request, 'admin.html', {'questions': questions})


@user_passes_test(is_admin)
def add_answer(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        answer_text = request.POST.get('answer_text')
        next_question_id = request.POST.get('next_question_id')
        create_answer(question_id, answer_text, next_question_id)
        return redirect('admin_panel')

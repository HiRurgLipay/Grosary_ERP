from django.shortcuts import render, redirect
from core.models import Question
from core.business.services import create_question, create_answer


def add_question(request):
    if request.method == 'POST':
        question_text = request.POST.get('question_text')
        create_question(question_text)
        return redirect('add_question')
    else:
        questions = Question.objects.all()
        return render(request, 'admin.html', {'questions': questions})


def add_answer(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        answer_text = request.POST.get('answer_text')
        next_question_id = request.POST.get('next_question_id')
        no_text = request.POST.get('no_text')
        if no_text:
            answer_text = None  
        create_answer(question_id, answer_text, next_question_id)
        return redirect('add_question')
    else:
        pass

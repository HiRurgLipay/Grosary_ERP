from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from core.business.services import show_answers_service


@login_required
def public_catering_view(request):
    _, question_answers = show_answers_service(request.user)
    return render(request, 'public_catering.html', {'question_answers': question_answers})


@login_required
def retail_view(request):
    _, question_answers = show_answers_service(request.user)
    return render(request, 'retail.html', {'question_answers': question_answers})


@login_required
def appointment_view(request):
    _, question_answers = show_answers_service(request.user)
    return render(request, 'appointment.html', {'question_answers': question_answers})

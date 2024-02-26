from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Question
from core.business.services import get_next_question


@login_required
def get_question(request, question_id, survey_id):
    user = request.user
    next_question = get_next_question(user, question_id)

    if isinstance(next_question, Question):
        options = next_question.options.all()
        return render(request, 'question.html', {'question': next_question, 'options': options, 'survey_id': survey_id})
    else:
        return render('error.html')
    
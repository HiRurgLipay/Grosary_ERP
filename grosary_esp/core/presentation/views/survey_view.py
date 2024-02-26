from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from core.business.services.survey_service import get_first_question, create_new_survey, get_last_survey, get_user_answers, determine_business_type


@login_required
def start_survey(request):
    first_question = get_first_question()
    survey = create_new_survey(request.user)
    return redirect('get_question', question_id=first_question.id, survey_id=survey.id)


@login_required
def survey_complete(request):
    user = request.user
    last_survey = get_last_survey(user)
    user_answers = get_user_answers(user, last_survey)
    business_type = determine_business_type(user_answers)

    if business_type == 'Общепит':
        return redirect('public_catering.html')
    elif business_type == 'Ритейл':
        return redirect('retail.html')
    elif business_type == 'Услуги по записи':
        return redirect('appointment.html')

    return render(request, 'error.html')
    
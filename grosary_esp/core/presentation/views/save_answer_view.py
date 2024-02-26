from django.shortcuts import redirect
from django.http import JsonResponse
from core.business.services import save_user_answer


def save_answer(request):
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        option_id = request.POST.get('option_id')
        survey_id = request.POST.get('survey_id')
        
        next_question, _ = save_user_answer(request.user, question_id, option_id, survey_id)
        
        if next_question:
            return redirect('get_question', question_id=next_question.id, survey_id=survey_id)
        else:
            return redirect('survey_complete')
    else:
        return JsonResponse({'error': 'Метод запроса должен быть POST'})
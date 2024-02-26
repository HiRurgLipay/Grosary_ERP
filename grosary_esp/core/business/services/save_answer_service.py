from django.shortcuts import get_object_or_404
from core.models import Survey, Question, AnswerOption, UserAnswer

def save_user_answer(user, question_id, option_id, survey_id):
    """
    Сохраняет ответ пользователя на вопрос.
    """
    survey = get_object_or_404(Survey, pk=survey_id)  # Используем survey_id
    question = get_object_or_404(Question, pk=question_id)
    option = get_object_or_404(AnswerOption, pk=option_id)
    UserAnswer.objects.create(user=user, question=question, answer_option=option, survey=survey)
    
    next_question = option.next_question
    return next_question, survey
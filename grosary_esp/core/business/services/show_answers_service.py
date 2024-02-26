from core.models import Survey, UserAnswer


def show_answers_service(user):
    user_surveys = Survey.objects.filter(user=user)
    question_answers = []
    
    if user_surveys.exists():
        last_survey = user_surveys.last()
        user_answers = UserAnswer.objects.filter(user=user, survey=last_survey)
        
        if user_answers.exists():
            question_answers = [(user_answer.question, user_answer.answer_option.text) for user_answer in user_answers]
    
    return user_surveys, question_answers

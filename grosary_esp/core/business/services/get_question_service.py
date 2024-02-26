from core.models import Question, UserAnswer

def get_next_question(user, question_id):
    """
    Возвращает следующий вопрос для пользователя.
    """
    current_question = Question.objects.get(pk=question_id)
    user_answers = UserAnswer.objects.filter(user=user)

    if current_question == Question.objects.first():
        return current_question

    if user_answers.exists():
        last_user_answer = user_answers.latest('created_at')
        next_question = last_user_answer.answer_option.next_question
    else:
        next_question = Question.objects.first()

    return next_question

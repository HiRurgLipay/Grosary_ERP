from core.models import Question, AnswerOption


def create_question(question_text):
    return Question.objects.create(text=question_text)


def create_answer(question_id, answer_text, next_question_id):
    question = Question.objects.get(pk=question_id)
    next_question = None
    if next_question_id:
        next_question = Question.objects.get(pk=next_question_id)
    return AnswerOption.objects.create(question=question, text=answer_text, next_question=next_question)

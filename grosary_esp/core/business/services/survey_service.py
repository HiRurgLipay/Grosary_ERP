from core.models import Survey, UserAnswer, Question


def create_survey(user):
    return Survey.objects.create(user=user)


def get_first_question():
    return Question.objects.first()


def create_new_survey(user):
    return create_survey(user)


def get_last_survey(user):
    return user.survey_set.last()


def get_user_answers(user, survey):
    return UserAnswer.objects.filter(user=user, survey=survey)


def determine_business_type(user_answers):
    business_type = None
    for user_answer in user_answers:
        if user_answer.question.text == 'Какой тип бизнеса?':
            business_type = user_answer.answer_option.text
            break
    return business_type

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'grosary_esp.settings')
django.setup()

from core.models import Survey, Question, Answer, DependentQuestion

def create_survey(title, description):
    return Survey.objects.get_or_create(title=title, description=description)[0]

def create_question(text, question_type, survey):
    return Question.objects.create(text=text, question_type=question_type, survey=survey)

def create_answer(text, question):
    return Answer.objects.create(text=text, question=question)

def create_dependent_question(text, parent_answer, next_question):
    return DependentQuestion.objects.create(text=text, parent_answer=parent_answer, next_question=next_question)

def main():
    survey = create_survey("Онбординг", "Опрос для новых компаний")
    
    # Вопросы 1 уровня
    question1 = create_question("Каким типом бизнеса вы владеете?", Question.SINGLE_CHOICE, survey)
    answer1_1 = create_answer("Общественное питание", question1)
    answer1_2 = create_answer("Ритейл", question1)
    answer1_3 = create_answer("Услуги по записи", question1)

    # Вопросы 2 уровня
    question2_1 = create_question("Какое направление у вашего заведения общественного питания?", Question.SINGLE_CHOICE, survey)
    answer2_1_1 = create_answer("Бар", question2_1)
    answer2_1_2 = create_answer("Кофейня", question2_1)
    answer2_1_3 = create_answer("Ресторан", question2_1)
    answer2_1_4 = create_answer("Бистро", question2_1)
    answer2_1_5 = create_answer("Бургерная", question2_1)

    question2_2 = create_question("Какой направление ритейла?", Question.SINGLE_CHOICE, survey)
    answer2_2_1 = create_answer("Продуктовый магазин", question2_2)
    answer2_2_2 = create_answer("Магазин одежды", question2_2)
    answer2_2_3 = create_answer("Аптека", question2_2)
    answer2_2_4 = create_answer("Электронный магазин", question2_2)

    question2_3 = create_question("Какие услуги по записи вы предоставляете?", Question.MULTIPLE_CHOICE, survey)
    answer2_3_1 = create_answer("Парикмахерские услуги", question2_3)
    answer2_3_2 = create_answer("Медицинские услуги", question2_3)
    answer2_3_3 = create_answer("Услуги красоты", question2_3)
    answer2_3_4 = create_answer("Услуги массажа", question2_3)
    
    # Зависимые вопросы
    dependent_question1 = create_question("Общая площадь помещения", Question.TEXT, survey)
    create_dependent_question("Бар", answer2_1_1, dependent_question1)
    create_dependent_question("Кофейня", answer2_1_2, dependent_question1)
    create_dependent_question("Ресторан", answer2_1_3, dependent_question1)
    create_dependent_question("Бистро", answer2_1_4, dependent_question1)
    create_dependent_question("Бургерная", answer2_1_5, dependent_question1)

    dependent_question2 = create_question("Количество посадочных мест", Question.TEXT, survey)
    create_dependent_question("Бар", answer2_1_1, dependent_question2)
    create_dependent_question("Кофейня", answer2_1_2, dependent_question2)
    create_dependent_question("Ресторан", answer2_1_3, dependent_question2)
    create_dependent_question("Бистро", answer2_1_4, dependent_question2)
    create_dependent_question("Бургерная", answer2_1_5, dependent_question2)

    dependent_question3 = create_question("Площадь залов для посетителей", Question.TEXT, survey)
    create_dependent_question("Бар", answer2_1_1, dependent_question3)
    create_dependent_question("Кофейня", answer2_1_2, dependent_question3)
    create_dependent_question("Ресторан", answer2_1_3, dependent_question3)
    create_dependent_question("Бистро", answer2_1_4, dependent_question3)
    create_dependent_question("Бургерная", answer2_1_5, dependent_question3)

    dependent_question4 = create_question("Площадь кухни", Question.TEXT, survey)
    create_dependent_question("Бар", answer2_1_1, dependent_question4)
    create_dependent_question("Кофейня", answer2_1_2, dependent_question4)
    create_dependent_question("Ресторан", answer2_1_3, dependent_question4)
    create_dependent_question("Бистро", answer2_1_4, dependent_question4)
    create_dependent_question("Бургерная", answer2_1_5, dependent_question4)

if __name__ == "__main__":
    main()

from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel
from .answer import AnswerOption
from .question import Question
from .survey import Survey


class UserAnswer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_option = models.ForeignKey(AnswerOption, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.question.text} - {self.answer_option.text}'
    
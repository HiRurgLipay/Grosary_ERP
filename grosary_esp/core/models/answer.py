from django.db import models
from .question import Question
from .base_model import BaseModel


class AnswerOption(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    next_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='previous_options', null=True, blank=True)

    def __str__(self):
        return self.text

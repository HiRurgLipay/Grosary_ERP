from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel


class Survey(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Survey for {self.user.username}'

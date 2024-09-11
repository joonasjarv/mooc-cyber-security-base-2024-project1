import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    votes_yes = models.IntegerField(default=0)
    votes_no = models.IntegerField(default=0)
    def __str__(self):
        return self.question_text

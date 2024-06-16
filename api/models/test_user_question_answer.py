from django.contrib.auth.models import User
from django.db import models

from api.models.question import Question
from api.models.answer import Answer


class TestUserQuestionAnswer(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, verbose_name="Вопрос", on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, verbose_name="Ответ", on_delete=models.CASCADE)

    def __str__(self):
        return self.question.title + " " + self.answer.text

    class Meta:
        verbose_name = 'Отправленные вопрос и ответ к тесту'
        verbose_name_plural = 'Отправленные вопрос и ответ к тесту'

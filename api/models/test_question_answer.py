from django.db import models

from question import Question
from test import Test


class TestQuestionAnswer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Пользователь")
    answer = models.BooleanField(verbose_name="Результат")

    def __str__(self):
        return self.test.title

    class Meta:
        verbose_name = 'Отправленный тест'
        verbose_name_plural = '6 Отправленные тесты'

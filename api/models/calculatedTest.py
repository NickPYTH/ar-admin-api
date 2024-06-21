from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

from api.models.test import Test
from api.models.test_user_question_answer import TestUserQuestionAnswer


class CalculatedTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")
    time = models.DateTimeField(verbose_name="Дата отправки", default=datetime.now())
    test_user_question_answer_list = models.ManyToManyField(TestUserQuestionAnswer,
                                                            related_name='test_user_question_answer_list',
                                                            verbose_name="Тест пользователь вопрос ответ")
    max_points = models.IntegerField(verbose_name="Максимальное кол-во баллов")
    user_points = models.IntegerField(verbose_name="Набранное кол-во баллов")

    def __str__(self):
        return '{0} {1}'.format(self.user.username, self.test.title)

    class Meta:
        verbose_name = 'Отправленный тест'
        verbose_name_plural = '6 Отправленные тесты'

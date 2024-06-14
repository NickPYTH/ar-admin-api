from django.contrib.auth.models import User
from django.db import models

from api.models.test import Test


class CalculatedTest(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    result = models.BooleanField(verbose_name="Результат")

    def __str__(self):
        return self.test.title

    class Meta:
        verbose_name = 'Отправленный тест'
        verbose_name_plural = '6 Отправленные тесты'

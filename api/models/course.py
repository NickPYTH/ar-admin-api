from django.db import models

from api.models.test import Test
from api.models.theory import Theory


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание", blank=True)
    theories = models.ManyToManyField(Theory, verbose_name="Обучающие статьи", blank=True)
    tests = models.ManyToManyField(Test, verbose_name="Тесты", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обучающий курс'
        verbose_name_plural = '1 Обучающие курсы'

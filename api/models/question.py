from django.db import models

from api.models.answer import Answer


class Question(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.CharField(max_length=250, verbose_name="Описание")
    answers = models.ManyToManyField(Answer, verbose_name="Ответы")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос для теста'
        verbose_name_plural = '4 Вопросы для тестов'
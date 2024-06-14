from django.db import models


class Answer(models.Model):
    text = models.CharField(max_length=150, verbose_name="Ответ")
    isCorrect = models.BooleanField(verbose_name="Правильный ответ")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = '5 Ответы на вопросы'

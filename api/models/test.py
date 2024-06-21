from datetime import datetime
from django.db import models

from api.models.profile import Profile
from api.models.question import Question


class Test(models.Model):
    order = models.IntegerField(default=0, verbose_name="Очередность в обучающем модуле")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.CharField(max_length=250, verbose_name="Описание")
    pub_date = models.DateTimeField(default=datetime.now(), verbose_name="Дата и время публикации")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Автор")
    questions = models.ManyToManyField(Question, verbose_name="Вопросы")
    pass_line = models.FloatField(default=0.6, verbose_name="Проходной процент(от 0 до 1)")

    def __str__(self):
        return self.id.__str__() + ' ' + self.title

    class Meta:
        verbose_name = 'Проверочный тест'
        verbose_name_plural = '3 Проверочные тесты'

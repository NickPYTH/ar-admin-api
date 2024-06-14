from datetime import datetime
from django.db import models

from api.models.profile import Profile


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Тело статьи")
    pub_date = models.DateTimeField(default=datetime.now(), verbose_name="Дата и время публикации")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обучающая статья Уст'
        verbose_name_plural = 'Обучающие статьи Уст'

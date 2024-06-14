from django.db import models


class Theory(models.Model):
    order = models.IntegerField(default=0, verbose_name="Очередность в обучающем модуле")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Тело статьи")

    def __str__(self):
        return str(self.order) + " " + self.title

    class Meta:
        verbose_name = 'Обучающая статья'
        verbose_name_plural = '2 Обучающие статьи'

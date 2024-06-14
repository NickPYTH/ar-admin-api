from django.db import models


class ArticleImage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Иллюстрация статьи'
        verbose_name_plural = 'Иллюстрации статей'

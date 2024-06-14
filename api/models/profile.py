from django.contrib.auth.models import User
from django.db import models

from api.models.achievement import Achievement


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    level = models.IntegerField(verbose_name="Уровень", default=0)
    achievements = models.ManyToManyField(Achievement, verbose_name="Достижения", blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

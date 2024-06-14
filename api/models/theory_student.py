from django.db import models

from api.models.profile import Profile
from api.models.theory import Theory


class TheoryStudent(models.Model):
    theory = models.ForeignKey(Theory, verbose_name="Статья", on_delete=models.CASCADE)
    student = models.ForeignKey(Profile, verbose_name="Студент", on_delete=models.CASCADE)

    def __str__(self):
        return self.theory.title + " " + self.student.user.username

    class Meta:
        verbose_name = 'Статьи и студенты'
        verbose_name_plural = 'Статьи и студенты'

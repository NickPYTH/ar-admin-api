from django.db import models

from api.models.profile import Profile


class StudentGroup(models.Model):
    teacher = models.ForeignKey(Profile, related_name='teacher', on_delete=models.CASCADE, verbose_name="Преподаватель")
    students = models.ManyToManyField(Profile, related_name='students', verbose_name="Студенты")

    def __str__(self):
        return "Учебная группа №"+str(self.id)

    class Meta:
        verbose_name = 'Учебный группы'
        verbose_name_plural = 'Учебные группы'

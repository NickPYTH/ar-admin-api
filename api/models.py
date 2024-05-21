from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Achievement(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.CharField(max_length=250, verbose_name="Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    level = models.IntegerField(verbose_name="Уровень", default=0)
    achievements = models.ManyToManyField(Achievement, verbose_name="Достижения", blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


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


class ArticleImage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Иллюстрация статьи'
        verbose_name_plural = 'Иллюстрации статей'


class ArticleFireWorks(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Тело статьи")
    pub_date = models.DateTimeField(default=datetime.now(), verbose_name="Дата и время публикации")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Огневая работа'
        verbose_name_plural = 'Огневые работы'


class Answer(models.Model):
    text = models.CharField(max_length=150, verbose_name="Ответ")
    isCorrect = models.BooleanField(verbose_name="Правильный ответ")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = '5 Ответы на вопросы'


class Question(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.CharField(max_length=250, verbose_name="Описание")
    answers = models.ManyToManyField(Answer, verbose_name="Ответы")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос для теста'
        verbose_name_plural = '4 Вопросы для тестов'


class Test(models.Model):
    order = models.IntegerField(default=0, verbose_name="Очередность в обучающем модуле")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.CharField(max_length=250, verbose_name="Описание")
    pub_date = models.DateTimeField(default=datetime.now(), verbose_name="Дата и время публикации")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Автор")
    questions = models.ManyToManyField(Question, verbose_name="Вопросы")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проверочный тест'
        verbose_name_plural = '3 Проверочные тесты'


class Theory(models.Model):
    order = models.IntegerField(default=0, verbose_name="Очередность в обучающем модуле")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    body = models.TextField(verbose_name="Тело статьи")

    def __str__(self):
        return str(self.order) + " " + self.title

    class Meta:
        verbose_name = 'Обучающая статья'
        verbose_name_plural = '2 Обучающие статьи'


class StudentGroup(models.Model):
    teacher = models.ForeignKey(Profile, related_name='teacher', on_delete=models.CASCADE, verbose_name="Преподаватель")
    students = models.ManyToManyField(Profile, related_name='students', verbose_name="Студенты")

    def __str__(self):
        return "Учебная группа №"+str(self.id)

    class Meta:
        verbose_name = 'Учебный группы'
        verbose_name_plural = 'Учебные группы'


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


class CalculatedTest(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    result = models.BooleanField(verbose_name="Результат")

    def __str__(self):
        return self.test.title

    class Meta:
        verbose_name = 'Отправленный тест'
        verbose_name_plural = '6 Отправленные тесты'

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class AchievementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'title', 'description')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    achievements = AchievementSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'level', 'achievements')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text', 'isCorrect')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'description', 'answers')


class TestSerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = ('id', 'title', 'description', 'pub_date', 'author', 'questions')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'pub_date', 'author')


class ArticleFireWorksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticleFireWorks
        fields = ('id', 'title', 'body', 'pub_date', 'author')


class CalculatedTestSerializer(serializers.HyperlinkedModelSerializer):
    test = TestSerializer()
    user = UserSerializer()

    class Meta:
        model = CalculatedTest
        fields = ('id', 'user', 'test', 'result')


class ArticleImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ('id', 'name', 'image')


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'description')

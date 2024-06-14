from rest_framework import serializers

from api.models.answer import Answer


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text', 'isCorrect')

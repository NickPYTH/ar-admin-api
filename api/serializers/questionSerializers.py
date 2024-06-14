from rest_framework import serializers

from api.models.question import Question
from api.serializers.answerSerializer import AnswerSerializer


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'description', 'answers')

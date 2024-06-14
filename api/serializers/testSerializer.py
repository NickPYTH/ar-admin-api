from rest_framework import serializers

from api.models.test import Test
from api.serializers.questionSerializers import QuestionSerializer


class TestSerializer(serializers.HyperlinkedModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = ('id', 'title', 'description', 'pub_date', 'author', 'questions', 'order')

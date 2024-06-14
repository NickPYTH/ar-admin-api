from rest_framework import serializers

from api.models.calculatedTest import CalculatedTest
from api.serializers.testSerializer import TestSerializer
from api.serializers.userSerializer import UserSerializer


class CalculatedTestSerializer(serializers.HyperlinkedModelSerializer):
    test = TestSerializer()
    user = UserSerializer()

    class Meta:
        model = CalculatedTest
        fields = ('id', 'user', 'test', 'result')

from rest_framework import serializers

from api.models.theory import Theory


class TheorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Theory
        fields = ('id', 'title', 'body', 'order', 'time')

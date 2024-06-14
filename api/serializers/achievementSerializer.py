from rest_framework import serializers

from api.models.achievement import Achievement


class AchievementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'title', 'description')
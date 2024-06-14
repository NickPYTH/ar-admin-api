from rest_framework import serializers

from api.models.profile import Profile
from api.serializers.achievementSerializer import AchievementSerializer
from api.serializers.userSerializer import UserSerializer


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    achievements = AchievementSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'level', 'achievements')

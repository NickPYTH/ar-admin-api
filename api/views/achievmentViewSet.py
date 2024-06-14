from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.achievement import Achievement
from api.serializers.achievementSerializer import AchievementSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [IsAuthenticated]

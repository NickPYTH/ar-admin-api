from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.answer import Answer
from api.serializers.answerSerializer import AnswerSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

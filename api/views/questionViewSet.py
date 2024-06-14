from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.question import Question
from api.serializers.questionSerializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

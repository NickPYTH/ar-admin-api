from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.theory import Theory
from api.serializers.theorySerializer import TheorySerializer


class TheoryViewSet(viewsets.ModelViewSet):
    queryset = Theory.objects.all()
    serializer_class = TheorySerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return self

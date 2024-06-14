from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models.calculatedTest import CalculatedTest
from api.models.test import Test
from api.serializers.calculatedTestSerializer import CalculatedTestSerializer


class CalculatedTestViewSet(viewsets.ModelViewSet):
    queryset = CalculatedTest.objects.all()
    serializer_class = CalculatedTestSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        test = CalculatedTest()
        test.test = Test.objects.get(id=data['test_id'])
        test.user = request.user
        test.result = data['result']
        test.save()
        return Response(status=200)

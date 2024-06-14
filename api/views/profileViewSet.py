from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.models.calculatedTest import CalculatedTest
from api.models.profile import Profile
from api.serializers.profileSerializer import ProfileSerializer
from api.serializers.userSerializer import UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        user_serialized = UserSerializer(user)
        response = user_serialized.data
        good = CalculatedTest.objects.filter(user=user, result=True)
        bad = CalculatedTest.objects.filter(user=user, result=False)
        response['goodTests'] = good.count()
        response['badTests'] = bad.count()
        return Response(response, status=200)

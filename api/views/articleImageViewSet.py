from django.http import FileResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models.articleImage import ArticleImage
from api.serializers.articleImageSerializer import ArticleImageSerializer


class ArticleImageViewSet(viewsets.ModelViewSet):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        image = ArticleImage.objects.get(name=kwargs.get("pk"))
        response = FileResponse(image.image)
        return response

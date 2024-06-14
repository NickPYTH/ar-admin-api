from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.articleFireWorks import ArticleFireWorks
from api.serializers.articleFireWorksSerializer import ArticleFireWorksSerializer


class ArticleFireWorksViewSet(viewsets.ModelViewSet):
    queryset = ArticleFireWorks.objects.all()
    serializer_class = ArticleFireWorksSerializer
    permission_classes = [IsAuthenticated]

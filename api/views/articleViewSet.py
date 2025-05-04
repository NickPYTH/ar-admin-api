from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.article import Article
from api.serializers.articleSerializer import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]




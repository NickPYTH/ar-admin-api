from rest_framework import serializers

from api.models.articleImage import ArticleImage


class ArticleImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ('id', 'name', 'image')

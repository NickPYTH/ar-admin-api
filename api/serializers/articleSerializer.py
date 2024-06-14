from rest_framework import serializers

from api.models.article import Article


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'pub_date', 'author')

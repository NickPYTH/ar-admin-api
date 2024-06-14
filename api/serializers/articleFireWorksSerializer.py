from rest_framework import serializers

from api.models.articleFireWorks import ArticleFireWorks


class ArticleFireWorksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArticleFireWorks
        fields = ('id', 'title', 'body', 'pub_date', 'author')

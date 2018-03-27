from rest_framework import serializers
from models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'text', 'archive', 'created_at', 'updated_at')
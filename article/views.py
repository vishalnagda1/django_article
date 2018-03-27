# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleSerializer


@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    articles = ArticleSerializer(articles, many=True)
    return Response({
        'articles': articles.data,
    })

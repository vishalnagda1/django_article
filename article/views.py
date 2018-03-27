# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
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
        'articles': articles.data
    })


@api_view(['GET'])
def show(request):
    try:
        article_id = request.query_params['id']
        article = Article.objects.get(id=article_id)
        article = ArticleSerializer(article)
        return Response({
            'article': article.data
        })
    except ObjectDoesNotExist as e:
        return Response({
            'error': 'Article not found.',
        }, status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({
            'error': 'Invalid params passed',
        }, status.HTTP_400_BAD_REQUEST)

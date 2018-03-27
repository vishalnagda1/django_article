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
        }, status.HTTP_422_UNPROCESSABLE_ENTITY)
    except Exception as e:
        return Response({
            'error': 'Invalid params passed',
            'type': str(type(e))
        }, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create(request):
    try:
        article_data = request.data['article']
        title = article_data['title']
        text = article_data['text']
        article = Article.objects.create(title=title, text=text)
        return Response({
            'article': ArticleSerializer(article).data
        }, status.HTTP_201_CREATED)
    except Exception as e:
        return Response({
            'error': 'Invalid request',
            'type': str(type(e))
        }, status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update(request):
    try:
        article_id = request.query_params['id']
        article_data = request.data['article']
        article = Article.objects.get(id=article_id)
        article.title = article_data['title']
        article.text = article_data['text']
        article.save()
        return Response({
            'article': ArticleSerializer(article).data,
        })
    except ObjectDoesNotExist as e:
        return Response({
            'error': 'Article not found.',
            'type': str(type(e))
        }, status.HTTP_422_UNPROCESSABLE_ENTITY)
    except Exception as e:
        return Response({
            'error': 'Invalid request',
            'type': str(type(e))
        }, status.HTTP_400_BAD_REQUEST)
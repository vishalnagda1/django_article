# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, default='')
    text = models.TextField(default='')

# -*- coding: utf-8 -*-
from django.db import models

from django_mysql.models import Model, JSONField

class User(Model):
    id_str = models.CharField(
        max_length=30
    )
    name = models.CharField(
        max_length=300
    )
    screen_name = models.CharField(
        max_length=300
    )
    location = models.CharField(
        max_length=300,
        null=True
    )
    url = models.CharField(
        max_length=3000,
        null=True
    )
    description = models.CharField(
        max_length=3000,
        null=True
    )
    verified = models.BooleanField(
        default=False,
        null=True
    )
    followers = models.IntegerField(
        default=0
    )
    statuses_count = models.IntegerField(
        default=0
    )
    created_at =  models.DateTimeField(
        default=None,
        null=True
    )
    profile_image_url = models.CharField(
        max_length=3000
    )

class Tweet(Model):
    id_str = models.CharField(
        max_length=30
    )
    credated_at = models.DateTimeField(
        default=None,
        null=True
    )
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )
    tag = models.CharField(
        max_length=300,
        default=None
    )
    text = models.CharField(
        max_length=280
    )
    in_reply_to_status_id = models.CharField(
        max_length=30,
        null=True
    )
    in_reply_to_user_id = models.CharField(
        max_length=30,
        null=True
    )
    in_reply_to_screen_name = models.CharField(
        max_length=300,
        null=True
    )
    geo = models.CharField(
        max_length=300,
        null=True
    )
    coordinates = models.CharField(
        max_length=300,
        null=True
    )
    place = models.CharField(
        max_length=3000,
        null=True
    )
    quoted_status_id = models.CharField(
        max_length=30,
        null=True
    )
    quoted_staus = models.ForeignKey(
        "Tweet",
        null=True,
        on_delete=models.SET_NULL
    )
    quoted_status_permalink = models.CharField(
        max_length=300,
        null=True
    )
    quote_count = models.IntegerField(
        default=0
    )
    reply_count  = models.IntegerField(
        default=0
    )
    retweet_count = models.IntegerField(
        default=0
    )
    favorite_count = models.IntegerField(
        default=0
    )
    entities = JSONField()


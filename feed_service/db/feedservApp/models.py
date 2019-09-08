# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=255)
    users = models.CharField(max_length=256)


class Question(models.Model):
    q_string = models.CharField(max_length=1024)
    topic = models.ForeignKey(Topic)
    createdby = models.CharField(max_length=255)
    createdon = models.DateTimeField(auto_now_add=True)
    answers = models.ManyToManyField('Answer', related_name="Answers_for_Questions")


class Answer(models.Model):
    a_string = models.CharField(max_length=1024)
    question = models.ForeignKey(Question, related_name="Questions_for_Answers")
    createdby = models.CharField(max_length=255)
    createdon = models.DateTimeField(auto_now_add=True)


class Upvote(models.Model):
    answer = models.ForeignKey(Answer)
    createdby = models.CharField(max_length=1024)
    createdon = models.DateTimeField(auto_now_add=True)


class Downvote(models.Model):
    answer = models.ForeignKey(Answer)
    createdby = models.CharField(max_length=1024)
    createdon = models.DateTimeField(auto_now_add=True)


class Notification(models.Model):
    notification_type = (("answer", "answer"),
                         ("other", "other"),)
    type = models.CharField(max_length=256, choices=notification_type)
    entity = models.CharField(max_length=12)
    actioned_entity = models.CharField(max_length=1024)
    done_by = models.CharField(max_length=1024)
    owner = models.CharField(max_length=1024)

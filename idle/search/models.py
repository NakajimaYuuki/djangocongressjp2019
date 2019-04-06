from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.forms import JSONField
from django.db import models


class Genere(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Idle(models.Model):

    idle = models.OneToOneField(User, on_delete=models.CASCADE)

    # 以下はPostgres のみのフィールド
    features = JSONField(blank=True, null=True)
    tags = ArrayField(models.CharField(max_length=200), blank=True)

    @property
    def name(self):
        return self.idle.username

    def __str__(self):
        return self.idle.username


class IdleGroup(models.Model):
    name = models.CharField(max_length=255)
    member = models.ManyToManyField(Idle)
    genere = models.ForeignKey(Genere, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


# 使いたいフィールド

# DurationField 期間とからしい
# list
# JSON
# image
# file

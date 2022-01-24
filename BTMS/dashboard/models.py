# from asyncio.windows_events import NULL
# from datetime import timezone
# import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser



class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'teams'


class Games(models.Model):
    id = models.AutoField(primary_key=True)
    round = models.CharField(max_length=255, blank=True, null=True,
                             db_index=True)
    playdate = models.DateTimeField(blank=True, null=True)
    team_1 = models.ForeignKey(Teams, on_delete=models.SET_NULL, blank=True,
                               null=True, related_name='team_1')
    team_2 = models.ForeignKey(Teams, on_delete=models.SET_NULL, blank=True,
                               null=True, related_name='team_2')

    class Meta:
        managed = True
        db_table = 'games'


class Users(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    last_name = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=128, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    height = models.BigIntegerField(blank=True, null=True)

    team = models.ForeignKey(Teams, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        managed = True
        db_table = 'users'


class Scores(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Games, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, blank=True, null=True)
    scores = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scores'


class SiteUsage(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    # action types: login, logout, start_view, end_view
    action_types = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, blank=True, null=True)
    session_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'site_usage'
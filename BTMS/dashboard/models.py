from datetime import timezone
import datetime
from pyexpat import model
from django.db import models

# Create your models here.

# For referene only
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


# Main Models


class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'teams'

class Games(models.Model):
    id = models.AutoField(primary_key=True)
    round = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    playdate = models.DateTimeField(blank=True, null=True)
    # team_1 = 
    # team_2 = 
    
    class Meta:
        managed = True
        db_table = 'games'


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    last_name = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=128, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    height = models.BigIntegerField(blank=True, null=True)

    team = models.OneToOneField(Teams)

    class Meta:
        ordering = ['last_name', 'first_name']
        managed = True
        db_table = 'users'

class Scores(models.Model):
    id = models.AutoField(primary_key=True)
    # game
    # user
    scores = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'scores'

class SiteUsage(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    # action types: login, logout, start_view, end_view
    action_types = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    
    # user
    # django_session

    class Meta:
        managed = True
        db_table = 'site_usage'
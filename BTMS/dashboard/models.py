# from asyncio.windows_events import NULL
# from datetime import timezone
# import datetime
from queue import Empty
from django.db import models
from django.contrib.auth.models import AbstractUser

from dashboard.services.contants import USERTYPES



class TeamsManager(models.Manager):

    def get_winner_teams(self, round):
        games = Games.objects.filter(round=round)
        winners = []
        for g in games:
            g: Games
            winners.append(g.get_winner_team())
        return winners

class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    objects = TeamsManager()

    class Meta:
        managed = True
        db_table = 'teams'

    def get_coach(self):
        coach = Users.objects.filter(role=USERTYPES.COACH, team=self)
        if coach is None:
            return None
        else:
            return coach.first()

    def get_all_players(self):
        all_players = Users.objects.filter(role=USERTYPES.PLAYER, team=self).order_by('id')
        return all_players


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

    def __get_scores(self, team):
        all_players = Users.objects.filter(team=team, role=USERTYPES.PLAYER)
        if all_players is None:
            return 0
        scores_sum = 0
        for p in all_players:
            scoreResult = Scores.objects.filter(game=self, user=p).first()
            if scoreResult is None:
                continue
            scores_sum += scoreResult.scores
        return scores_sum

    def get_team1_scores(self):
        return self.__get_scores(self.team_1)

    def get_team2_scores(self):
        return self.__get_scores(self.team_2)

    def get_winner_team(self):
        if self.get_team1_scores() > self.get_team2_scores():
            return self.team_1
        else:
            return self.team_2


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


class ScoresManager(models.Manager):
    def delete_everything(self):
        Scores.objects.all().delete()


class Scores(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Games, on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, blank=True, null=True)
    scores = models.BigIntegerField(blank=True, null=True)

    objects = ScoresManager()

    class Meta:
        managed = True
        db_table = 'scores'


class SiteUsage(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(blank=True, null=True)
    # action types: login, logout, start_view, end_view
    action_types = models.CharField(max_length=255, blank=True, null=True, db_index=True)

    user = models.ForeignKey(Users, on_delete=models.SET_NULL, blank=True, null=True)
    session_key = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'site_usage'

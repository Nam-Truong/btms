
from datetime import date
from tkinter import ROUND
from django.test import TestCase
from dashboard.services.set_db import create_new_tournament
from dashboard.services.contants import ROUNDS, USERTYPES, COMMON_AUTH_PASS,\
     TOTAL_PLAYERS, TOTAL_COACHES, TOTAL_ADMINS, TOTAL_GAMES_IN_ROUND1,\
     TOTAL_PLAYERS_PER_TEAM, MIN_PLAYERS_ON_A_GAME, TOTAL_GAMES_IN_ROUND2,\
     TOTAL_GAMES_IN_ROUND3, TOTAL_GAMES_IN_ROUND4
from dashboard.models import Users, Teams, Games, Scores


class SetDBTestCase(TestCase):
    def tearDown(self) -> None:
        super().tearDown()

    def test_create_new_tournament(self):
        upto_round = ROUNDS.ROUND_4
        create_new_tournament(upto_round)

        # Verify players setup
        all_players = Users.objects.filter(role=USERTYPES.PLAYER)\
                           .order_by('id')

        self.assertEquals(len(all_players), TOTAL_PLAYERS)
        for p in all_players:
            print('PlayerId %s: username=%s; full name is "%s"' %
                  (p.id, p.username, p.get_full_name()))
            self.assertEquals(p.password, COMMON_AUTH_PASS)
            self.assertTrue(p.team is not None)
            print('- teamId=%s; teamName=%s' % (p.team.id, p.team.name))

        # Verify coach setup
        all_coachs = Users.objects.filter(role=USERTYPES.COACH)\
                          .order_by('id')
        self.assertEquals(len(all_coachs), TOTAL_COACHES)
        for c in all_coachs:
            print('CoachId %s: username=%s; full name is "%s"' %
                  (c.id, c.username, c.get_full_name()))
            self.assertEquals(c.password, COMMON_AUTH_PASS)
            self.assertTrue(c.team is not None)
            print('- teamId=%s; teamName=%s' % (c.team.id, c.team.name))

        # Verify admin setup
        all_admins = Users.objects.filter(role=USERTYPES.ADMIN)\
                          .order_by('id')
        self.assertEquals(len(all_admins), TOTAL_ADMINS)
        for a in all_admins:
            print('AdminId %s: username=%s; full name is "%s"' %
                  (a.id, a.username, a.get_full_name()))
            self.assertEquals(a.password, COMMON_AUTH_PASS)
            self.assertTrue(a.team is None)

        # Verify team setup
        all_teams = Teams.objects.all().order_by('id')
        self.assertEquals(len(all_teams), TOTAL_COACHES)
        for t in all_teams:
            t: Teams
            print('%s. Team "%s":' % (t.id, t.name))
            team_coach: Users = t.get_coach()
            self.assertIsNotNone(team_coach)
            print('  + Coach: id=%s, name="%s"' % (team_coach.id, team_coach.get_full_name()))
            team_players = t.get_all_players()
            self.assertIsNotNone(team_players)
            for tp in team_players:
                self.assertTrue(type(tp) is Users)
                tp: Users
                print('  + Player: id=%s, name="%s"' % (tp.id, tp.get_full_name()))

        # Verify round-1 games setup
        all_round1_games = Games.objects.filter(round=ROUNDS.ROUND_1)\
                                .order_by('id')
        self.assertEquals(len(all_round1_games), TOTAL_GAMES_IN_ROUND1)
        for g in all_round1_games:
            self.assertTrue(type(g) is Games)
            g: Games
            print('#GameId %s on %s: "%s" vs "%s" with scores %s-%s' %
                  (g.id, g.playdate.date(), g.team_1.name, g.team_2.name,
                   g.get_team1_scores(), g.get_team2_scores()))
            print('  - Winner is "%s"' % (g.get_winner_team().name))

            on_game_team1_players_scores = Scores.objects.filter(game=g, user__team=g.team_1)
            on_game_team2_players_scores = Scores.objects.filter(game=g, user__team=g.team_2)
            self.assertIsNotNone(on_game_team1_players_scores)
            self.assertIsNotNone(on_game_team2_players_scores)
            self.assertTrue(len(on_game_team1_players_scores)in range(MIN_PLAYERS_ON_A_GAME, TOTAL_PLAYERS_PER_TEAM))
            self.assertTrue(len(on_game_team2_players_scores)in range(MIN_PLAYERS_ON_A_GAME, TOTAL_PLAYERS_PER_TEAM))
            print('  - %s players of "%s" played the game.' % (len(on_game_team1_players_scores), g.team_1.name))
            team1_scores = 0
            team2_scores = 0
            for ps in on_game_team1_players_scores:
                ps: Scores
                print('    ."%s" scored %s.' % (ps.user.get_full_name(), ps.scores))
                team1_scores += ps.scores

            print('  - %s players of "%s" played the game.' % (len(on_game_team2_players_scores), g.team_2.name))
            for ps in on_game_team2_players_scores:
                ps: Scores
                print('    ."%s" scored %s.' % (ps.user.get_full_name(), ps.scores))
                team2_scores += ps.scores

            self.assertEquals(team1_scores, g.get_team1_scores())
            self.assertEquals(team2_scores, g.get_team2_scores())
        round1_winners = Teams.objects.get_winner_teams(ROUNDS.ROUND_1)
        print('Round-1 Winners are:')
        for rw in round1_winners:
            print('- %s' % (rw.name))

        # Verify round-2 games setup
        all_round2_games = Games.objects.filter(round=ROUNDS.ROUND_2)\
                                .order_by('id')
        self.assertEquals(len(all_round2_games), TOTAL_GAMES_IN_ROUND2)
        self.print_game_info(all_round2_games, ROUNDS.ROUND_2)

        # Verify round-3 games setup
        all_round3_games = Games.objects.filter(round=ROUNDS.ROUND_3)\
                                .order_by('id')
        self.assertEquals(len(all_round3_games), TOTAL_GAMES_IN_ROUND3)
        self.print_game_info(all_round3_games, ROUNDS.ROUND_3)

        # Verify round-4 games setup
        all_round4_games = Games.objects.filter(round=ROUNDS.ROUND_4)\
                                .order_by('id')
        self.assertEquals(len(all_round4_games), TOTAL_GAMES_IN_ROUND4)
        self.print_game_info(all_round4_games, ROUNDS.ROUND_4)

    
    def print_game_info(self, game_queryset, round):
        round_winners = []
        for g in game_queryset:
            self.assertTrue(type(g) is Games)
            g: Games
            print('#GameId %s on %s: "%s" vs "%s" with scores %s-%s' %
                  (g.id, g.playdate.date(), g.team_1.name, g.team_2.name,
                   g.get_team1_scores(), g.get_team2_scores()))
            print('  - Winner is "%s"' % (g.get_winner_team().name))
            round_winners.append(g.get_winner_team())

        
        print('%s Winners are:' % (round))
        for rw in round_winners:
            print('- %s' % (rw.name))
            


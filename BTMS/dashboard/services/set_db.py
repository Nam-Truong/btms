import random
from dashboard.services.contants import SAMPLE_FIRST_NAMES, SAMPLE_LAST_NAMES,\
    TOTAL_GAMES_IN_ROUND1, SIMUATED_PLAYDATE, MIN_PLAYERS_ON_A_GAME,\
    TOTAL_GAMES_IN_ROUND2, TOTAL_GAMES_IN_ROUND3, TOTAL_GAMES_IN_ROUND4
from dashboard.models import Users, Teams, Scores, Games, SiteUsage
from dashboard.services.contants import COMMON_AUTH_PASS, ROUNDS,\
     TOTAL_COACHES, TOTAL_PLAYERS, USERNAMES, USERTYPES, TEAM_NAMES,\
     TOTAL_PLAYERS_PER_TEAM


def create_new_user_with_random_name(username, password, user_type) -> Users:
    sample_firstname_index = random.randint(0, len(SAMPLE_FIRST_NAMES) - 1)
    sample_lastname_index = random.randint(0, len(SAMPLE_LAST_NAMES) - 1)
    random_height = random.randint(168, 210)  # measured in cm
    user = Users.objects.create(
                    username=username,
                    first_name=SAMPLE_FIRST_NAMES[sample_firstname_index],
                    last_name=SAMPLE_LAST_NAMES[sample_lastname_index],
                    role=user_type,
                    height=random_height,
                    password=password)
    return user


def create_new_team(name, description) -> Teams:
    team = Teams.objects.create(name=name, description=description)
    return team


def create_new_game(round, game_id, team_1, team_2):
    playdate = SIMUATED_PLAYDATE.get_playdate(round, game_id)
    game = Games.objects.create(round=round, team_1=team_1, team_2=team_2, 
                                playdate=playdate)
    return game


def create_new_site_usage_record(action_type, user: Users, timestamp):
    # TODO
    return None


def create_new_tournament(completed_round: ROUNDS):
    # Create 16 teams
    for team_name in TEAM_NAMES:
        create_new_team(team_name, '')

    all_teams = Teams.objects.all()

    # Create all coaches:
    for i in range(TOTAL_COACHES):
        create_new_user_with_random_name(
            USERNAMES.generate_coach_username(i + 1),
            COMMON_AUTH_PASS,
            USERTYPES.COACH)

    all_coachs = Users.objects.filter(role=USERTYPES.COACH).order_by('id')

    # 1. Create new users, including 160 players
    players_count = 0
    for i in range(TOTAL_PLAYERS):
        player = create_new_user_with_random_name(
            USERNAMES.generate_player_username(i + 1),
            COMMON_AUTH_PASS,
            USERTYPES.PLAYER)
        team_index = int(players_count / TOTAL_PLAYERS_PER_TEAM)
        current_team = all_teams[team_index]
        current_coach = all_coachs[team_index]
        player.team = current_team
        current_coach.team = current_team
        current_coach.save()
        player.save()
        players_count += 1

    # 1.c create 1 admin
    create_new_user_with_random_name(USERNAMES.ADMIN_USERNAME,
                                     COMMON_AUTH_PASS,
                                     USERTYPES.ADMIN)

    # 3. Create games and scores up to the completed round
    setup_new_tournament_scores_in_db(completed_round)

    return


def setup_new_tournament_scores_in_db(completed_round: ROUNDS):
    delete_scores_table()

    if completed_round == ROUNDS.ROUND_1:
        setup_tournament_scores_upto_round_1()
    elif completed_round == ROUNDS.ROUND_2:
        setup_tournament_scores_upto_round_2()
    elif completed_round == ROUNDS.ROUND_3:
        setup_tournament_scores_upto_round_3()
    else:
        setup_tournament_scores_upto_round_4()

    return


def delete_scores_table():
    Scores.objects.delete_everything()
    return


def simulate_game_scores(game, team: Teams):
    if game is None or team is None \
       or (game.team_1 != team and game.team_2 != team):
        return
    
    # Suppose that not every player did play a game
    # So, randomly create total number of players did play the game.
    total_players_on_game = random.randint(MIN_PLAYERS_ON_A_GAME + 1, TOTAL_PLAYERS_PER_TEAM - 1)
    all_players = team.get_all_players()
    players_list = []
    for p in all_players:
        players_list.append(p)
    
    random.shuffle(players_list)
    for i in range(total_players_on_game):
        p = players_list[i]
        simulated_scores = random.randint(0, 30)
        Scores.objects.create(game=game, user=p, scores=simulated_scores)


def simulate_game_scores_in_a_round(all_participating_teams, total_round_games, round):
    for i in range(total_round_games):
        team_1 = all_participating_teams[i*2]
        team_2 = all_participating_teams[i*2 + 1]
        game = create_new_game(round, i, team_1, team_2)
        simulate_game_scores(game, team_1)
        simulate_game_scores(game, team_2)


def setup_tournament_scores_upto_round_1():
    '''Simulate scores for round-1 with 16 teams and 8 games
    '''
    all_teams = Teams.objects.all()
    simulate_game_scores_in_a_round(all_teams, TOTAL_GAMES_IN_ROUND1, ROUNDS.ROUND_1)


def setup_tournament_scores_upto_round_2():
    '''Simulate scores for round-2 with 8 teams and 4 games
    '''
    setup_tournament_scores_upto_round_1()
    # Simulate scores for round-2
    round_1_winner_teams = Teams.objects.get_winner_teams(ROUNDS.ROUND_1)
    simulate_game_scores_in_a_round(round_1_winner_teams,
                                    TOTAL_GAMES_IN_ROUND2, ROUNDS.ROUND_2)
    return


def setup_tournament_scores_upto_round_3():
    setup_tournament_scores_upto_round_2()
    # Simulate scores for round-3
    round_2_winner_teams = Teams.objects.get_winner_teams(ROUNDS.ROUND_2)
    simulate_game_scores_in_a_round(round_2_winner_teams,
                                    TOTAL_GAMES_IN_ROUND3, ROUNDS.ROUND_3)
    return


def setup_tournament_scores_upto_round_4():
    setup_tournament_scores_upto_round_3()

    # Simulate scores for round-4
    round_3_winner_teams = Teams.objects.get_winner_teams(ROUNDS.ROUND_3)
    simulate_game_scores_in_a_round(round_3_winner_teams,
                                    TOTAL_GAMES_IN_ROUND4, ROUNDS.ROUND_4)
    return


def wipe_out_database():
    Scores.objects.all().delete()
    Users.objects.all().delete()
    Games.objects.all().delete()
    Teams.objects.all().delete()
    SiteUsage.objects.all().delete()

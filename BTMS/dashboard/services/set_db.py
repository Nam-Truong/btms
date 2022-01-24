

from asyncio.windows_events import NULL

from dashboard.models import Users
from dashboard.services.contants import COMMON_AUTH_PASS, ROUNDS, TOTAL_COACHES, TOTAL_PLAYERS, USERNAMES, USERTYPES


def create_new_user(username, password, user_type) -> Users:
    # TODO: create a new user with specified username, password, user_type and random info
    user: Users = Users.objects.create(username=username, first_name=random_first_name, last_name=random_last_name, role=user_type)
    
    return user

def create_new_team(name, description):
    # TODO
    return NULL

def create_new_game():
    # TODO
    return NULL

def create_new_scores():
    # TODO
    return NULL

def create_new_site_usage_record(action_type, user: Users, timestamp):
    # TODO
    return NULL

def create_new_tournament(completed_round: ROUNDS):

    # 1. Create new users, including 160 players, 10 coaches, 1 tournament admin
    # 1.a create 160 players:
    for i in range(TOTAL_PLAYERS):
        create_new_user(USERNAMES.generate_player_username(i + 1), COMMON_AUTH_PASS, USERTYPES.PLAYER)

    # 1.b create 10 coaches:
    for i in range(TOTAL_COACHES):
        create_new_user(USERNAMES.generate_coach_username(i + 1), COMMON_AUTH_PASS, USERTYPES.COACH)

    # 1.c create 1 admin
    create_new_user(USERNAMES.ADMIN_USERNAME, COMMON_AUTH_PASS, USERTYPES.ADMIN)

    # TODO 
    # 2. Create 16 teams, each of which has 10 players and 1 coach
    # create_new_team(name, description):

    # TODO
    # 3. Create games and scores up to the completed round

    return NULL




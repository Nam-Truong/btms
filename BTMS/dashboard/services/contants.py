
class USERTYPES:
    ADMIN = 'admin'
    PLAYER = 'player'
    COACH = 'coach'


class USERNAMES:
    ADMIN_USERNAME = 'admin'

    @staticmethod
    def generate_player_username(player_ordering_index):
        return PLAYER_USERNAME_PREFIX + str(player_ordering_index)

    @staticmethod
    def generate_coach_username(coach_ordering_index):
        return COACH_USERNAME_PREFIX + str(coach_ordering_index)


class ROUNDS:
    ROUND_1 = '1'
    ROUND_2 = '2'
    ROUND_3 = '3'
    ROUND_4 = 'Final'


PLAYER_USERNAME_PREFIX = 'player'
COACH_USERNAME_PREFIX = 'coach'
COMMON_AUTH_PASS = 'pbkdf2_sha256$260000$8LNVwvhW4meFnHiW5lWibP$UXfPzdYTjCPkzulDNUDkB7JHNI/6YN1ubVoxuPKgRN8='

TOTAL_PLAYERS = 160
TOTAL_PLAYERS_PER_TEAM = 10
TOTAL_COACHES = 16
TOTAL_ADMINS = 1

MIN_PLAYERS_ON_A_GAME = 5

TOTAL_GAMES_IN_ROUND1 = int(TOTAL_COACHES / 2)
TOTAL_GAMES_IN_ROUND2 = int(TOTAL_GAMES_IN_ROUND1 / 2)
TOTAL_GAMES_IN_ROUND3 = int(TOTAL_GAMES_IN_ROUND2 / 2)
TOTAL_GAMES_IN_ROUND4 = int(TOTAL_GAMES_IN_ROUND3 / 2)

class SIMUATED_PLAYDATE:

    @staticmethod
    def get_playdate(round, game_id):
        ''' game_id is Zero-based index.
        '''
        from datetime import timedelta
        from django.utils import timezone

        substracted_days = SIMUATED_PLAYDATE.__get_days_to_substract(round)
        round_start_date = timezone.now() - timedelta(days=substracted_days)
        relative_game_date = SIMUATED_PLAYDATE.__get_relative_game_date(round, game_id)
        return round_start_date + timedelta(days=relative_game_date)

    @staticmethod
    def __get_relative_game_date(round, game_id):
        ''' game_id is Zero-based index.
        '''
        if round == ROUNDS.ROUND_1:
            return 2 * game_id
        elif round == ROUNDS.ROUND_2:
            return 4 * game_id
        elif round == ROUNDS.ROUND_3:
            return 7 * game_id
        else:
            return 0

    @staticmethod
    def __get_days_to_substract(round):
        if round == ROUNDS.ROUND_1:
            return 90
        elif round == ROUNDS.ROUND_2:
            return 60
        elif round == ROUNDS.ROUND_3:
            return 30
        else:
            return 2


TEAM_NAMES = [
    'Dragon',
    'Tiger',
    'Snake',
    'Horse',
    'Unicorn',
    'Banana',
    'Rats',
    'Crows',
    'Buffalo',
    'Butterfly',
    'Goat',
    'Wings',
    'Pigs',
    'Cats',
    'Monkeys',
    'Rooster'
]
SAMPLE_FIRST_NAMES = [
                        'Robert',
                        'John',
                        'Michael',
                        'William',
                        'David',
                        'Richard',
                        'Joseph',
                        'Thomas',
                        'Charles',
                        'Christopher',
                        'Daniel',
                        'Matthew',
                        'Anthony',
                        'Mark',
                        'Donald',
                        'Steven',
                        'Paul',
                        'Andrew',
                        'Joshua',
                        'Kenneth',
                        'Kevin',
                        'Brian',
                        'George',
                        'Edward',
                        'Ronald',
                        'Timothy',
                        'Jason',
                        'Jeffrey',
                        'Ryan',
                        'Jacob',
                        'Gary',
                        'Nicholas',
                        'Eric',
                        'Jonathan',
                        'Stephen',
                        'Larry',
                        'Justin',
                        'Scott',
                        'Brandon',
                        'Benjamin',
                        'Samuel']

SAMPLE_LAST_NAMES = [
                        'Gregory',
                        'Frank',
                        'Alexander',
                        'Raymond',
                        'Patrick',
                        'Jack',
                        'Dennis',
                        'Jerry',
                        'Tyler',
                        'Aaron',
                        'Jose',
                        'Adam',
                        'Henry',
                        'Nathan',
                        'Douglas',
                        'Zachary',
                        'Peter',
                        'Kyle',
                        'Walter',
                        'Ethan',
                        'Jeremy',
                        'Harold',
                        'Keith',
                        'Christian',
                        'Roger',
                        'Noah',
                        'Gerald',
                        'Carl',
                        'Terry',
                        'Sean',
                        'Austin',
                        'Arthur',
                        'Lawrence',
                        'Jesse',
                        'Dylan',
                        'Bryan',
                        'Joe',
                        'Jordan',
                        'Billy',
                        'Bruce',
                        'Albert',
                        'Willie',
                        'Gabriel',
                        'Logan',
                        'Alan',
                        'Juan',
                        'Wayne',
                        'Roy',
                        'Ralph',
                        'Randy',
                        'Eugene',
                        'Vincent',
                        'Russell',
                        'Elijah',
                        'Louis',
                        'Bobby',
                        'Philip',
                        'Johnny']

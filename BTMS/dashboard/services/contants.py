
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
TOTAL_COACHES = 10
TOTAL_ADMINS = 1


SAMPLE_FIRST_NAMES = ['Robert',
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

SAMPLE_LAST_NAMES = ['Gregory',
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

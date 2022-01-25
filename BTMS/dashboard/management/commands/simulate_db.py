from django.core.management.base import BaseCommand

from dashboard.services.set_db import create_new_tournament

class Command(BaseCommand):
    help = 'Simulate data of players, coach, admin, games up to a desired round, i.e. {1, 2, 3, 4}'

    def add_arguments(self, parser):
        parser.add_argument('round', nargs='+', type=int ) 

    def handle(self, *args, **options):
        upto_round = options['round']
        self.stdout.write(self.style.SUCCESS(f'Entered round is {upto_round}'))
        create_new_tournament(upto_round)

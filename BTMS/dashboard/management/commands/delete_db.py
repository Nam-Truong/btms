from django.core.management.base import BaseCommand

from dashboard.services.set_db import wipe_out_database

class Command(BaseCommand):
    help = 'Delete all simulated data of players, coach, admin, games, etc. in database.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        wipe_out_database()
        self.stdout.write(self.style.SUCCESS(f'Already wiped out all data in DB.'))

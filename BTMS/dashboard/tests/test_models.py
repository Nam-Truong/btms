
from django.test import TestCase
from dashboard.models import Scores


class ModelsTestCase(TestCase):
    def tearDown(self) -> None:
        super().tearDown()

    def test_delete_all_scores(self):
        Scores.objects.delete_everything()


from django.test import TestCase
from dashboard.models import Users
from dashboard.services.auth import authenticate_user
from dashboard.services.contants import USERTYPES


class AuthTestCase(TestCase):

    def tearDown(self) -> None:
        super().tearDown()

    def test_authenticate_user(self):
        username = 'test_user'
        user: Users = Users.objects.create(username=username,
                                           first_name='nam',
                                           last_name='truong',
                                           role=USERTYPES.PLAYER)
        raw_pwd = 'haoc32&32'
        user.set_password(raw_pwd)
        user.save()

        loaded_user = Users.objects.get(username=username)

        self.assertIsNotNone(loaded_user)
        self.assertTrue(type(loaded_user) is Users)

        print('- hashed-pwd: ' + loaded_user.password)
        print('- username: ' + loaded_user.username)
        print('- first name: ' + loaded_user.first_name)
        print('- last name: ' + loaded_user.last_name)
        print('- role: ' + loaded_user.role)

        self.assertTrue(loaded_user.check_password(raw_pwd))
        self.assertEquals('nam', loaded_user.first_name)
        self.assertEquals('truong', loaded_user.last_name)
        self.assertEquals('test_user', loaded_user.username)
        self.assertEquals(USERTYPES.PLAYER, loaded_user.role)

        self.assertTrue(authenticate_user(loaded_user.username, raw_pwd))

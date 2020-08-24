from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.contrib import auth

from django.contrib.auth.models import User
from . import views


class IndexPageTests(SimpleTestCase):

    def test_index_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 302)


class UserProfilePageTest(TestCase):
    """
    test '/' url
    Inhereit from TestCase, will run order by subclasses

    test_* will be run
    """

    def setUp(self):
        # create super user
        self.user = User.objects.create_superuser(
            username='testadmin',
            email='admin@test.com',
            password='password_test')
        self.user.save()

    def test_index_page(self):
        # before login
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

        # after login
        self.client.force_login(user=self.user)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        assert b'Logout' in response.content

        # after logout
        self.client.logout()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_user_detail_page(self):
        self.client.force_login(user=self.user)
        response = self.client.get('/user/' + self.user.username + '/')
        self.assertEqual(response.status_code, 200)

        # check leaflet exist
        assert b'leaflet-container' in response.content

    def test_map_page(self):
        response = self.client.get('/map/')
        self.assertEqual(response.status_code, 200)

        # check leaflet exist
        assert b'leaflet-container' in response.content


class TestAdminPage(TestCase):
    def create_superuser(self):
        self.username_admin = 'testadmin'
        self.password_admin = 'password_test'
        self.user_admin = User.objects.create_superuser(
            username=self.username_admin,
            email='admin@test.com',
            password=self.password_admin)
        self.user_admin.is_staff = True
        self.user_admin.is_superuser = True
        self.user_admin.is_active = True
        self.user_admin.save()

    def create_staffuser(self):
        self.username_staff = 'teststaff'
        self.password_staff = 'password_test'
        self.user_staff = User.objects.create(
            username=self.username_staff,
            email='staff@test.com',
            password=self.password_staff)
        self.user_staff.is_staff = True
        self.user_staff.is_superuser = False
        self.user_staff.is_active = True
        self.user_staff.save()

    def create_user(self):
        self.username = 'testuser'
        self.password = 'password_test'
        self.user = User.objects.create(
            username=self.username,
            email='user@test.com',
            password=self.password)
        self.user.is_staff = False
        self.user.is_superuser = False
        self.user.is_active = True
        self.user.save()

    def test_profile_admin_superuser(self):
        """
        Test superuser
        """
        self.create_superuser()
        client = Client()
        client.login(username=self.username_admin,
            password=self.password_admin)

        user = auth.get_user(client)
        self.assertTrue(user.is_authenticated)

        admin_pages = [
            "/admin/",
            "/admin/auth/",
            "/admin/auth/group/",
            "/admin/auth/group/add/",
            "/admin/auth/user/",
            "/admin/auth/user/add/",
            "/admin/password_change/"
        ]
        for page in admin_pages:
            response = client.get(page)
            assert response.status_code == 200
            assert b"<!DOCTYPE html" in response.content

    def test_profile_admin_staff(self):
        """
        Test staff
        """
        self.create_staffuser()

        client = Client()
        client.force_login(user=self.user_staff)

        user = auth.get_user(client)
        self.assertEqual(user.is_authenticated, True)

        response = client.get('/admin/')
        self.assertEqual(response.status_code, 200)

        response = client.get('"/admin/auth/user/add/"')
        assert response.status_code != 200

    def test_profile_admin_user(self):
        """
        Test non-staff user
        """
        self.create_user()
        client = Client()
        client.force_login(user=self.user)

        user = auth.get_user(client)
        self.assertEqual(user.is_authenticated, True)

        response = client.get('/admin/')
        assert response.status_code != 200


class TestAlwaysFail(TestCase):
    def test_always_fail(self):
        assert False

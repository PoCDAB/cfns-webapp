from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
def API_POST_AIS_TEST(TestCase):

    @classmethod
    def setUpClass(cls):

        cls.user = User.objects.create_user(username="admin",email="admin@admin.nl", password="admin", firstname= "Admin", lastname= 'Admin' )
        cls.user.save()
        cls.token = None
        # Create variables needed for tests
        cls.client = Client(HTTP_HOST='http://localhost:8000')

    def test_get_token(self):
        response = self.client.post(reverse('token'),data={'email': self.user.email, 'password': 'admin'}, format='text/html')
        self.token = response.data
        print(response.data)
        self.assertTrue('token' in self.token)
        self.assertEqual(response.status_code, 200)

    # def test_use_token(self):
    #     response = self.client.post(reverse('token'),header={'email': self.user.email, 'password': 'Corona'}, format='text/html')
    #     cls.token = response.data
    #     self.assertTrue('token' in token)
    #     self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        pass   
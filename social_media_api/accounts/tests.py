from django.test import TestCase
# accounts/tests.py
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

class FollowFeedTests(APITestCase):
    def setUp(self):
        self.u1 = User.objects.create_user(username='u1', password='pass')
        self.u2 = User.objects.create_user(username='u2', password='pass')
        self.u3 = User.objects.create_user(username='u3', password='pass')

        # u2 and u3 each create a post
        self.client.login(username='u2', password='pass')
        Post.objects.create(author=self.u2, title='t2', content='c2')
        self.client.logout()

        self.client.login(username='u3', password='pass')
        Post.objects.create(author=self.u3, title='t3', content='c3')
        self.client.logout()

    def test_follow_and_feed(self):
        # u1 follows u2
        self.client.login(username='u1', password='pass')
        res = self.client.post(f'/api/accounts/follow/{self.u2.id}/')
        self.assertEqual(res.status_code, 200)
        # feed should show u2 post
        res = self.client.get('/api/feed/')
        self.assertEqual(res.status_code, 200)
        self.assertGreaterEqual(len(res.data['results']), 1)

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment

class CommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u1", password="pass12345")
        self.other = User.objects.create_user(username="u2", password="pass12345")
        self.post = Post.objects.create(title="T", content="C", author=self.user)
        self.comment = Comment.objects.create(post=self.post, author=self.user, content="hi")

    def test_create_comment_requires_login(self):
        url = reverse("comment-create", kwargs={"post_pk": self.post.pk})
        resp = self.client.post(url, {"content": "new comment"})
        # redirect to login
        self.assertNotEqual(resp.status_code, 200)
        self.client.login(username="u2", password="pass12345")
        resp = self.client.post(url, {"content": "new comment"}, follow=True)
        self.assertContains(resp, "new comment")

    def test_edit_comment_only_author(self):
        url = reverse("comment-update", kwargs={"pk": self.comment.pk})
        self.client.login(username="u2", password="pass12345")
        resp = self.client.get(url)
        self.assertNotEqual(resp.status_code, 200)
        self.client.login(username="u1", password="pass12345")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_delete_comment_only_author(self):
        url = reverse("comment-delete", kwargs={"pk": self.comment.pk})
        self.client.login(username="u2", password="pass12345")
        resp = self.client.post(url)
        self.assertNotEqual(resp.status_code, 200)
        self.client.login(username="u1", password="pass12345")
        resp = self.client.post(url, follow=True)
        self.assertNotContains(resp, "hi")


# Create your tests here.

from datetime import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from pytz import UTC
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from blog.models import Post


class PostApiTestCase(TestCase):
    def setUp(self):
        self.u1 = get_user_model().objects.create_user(
            email="test@example.com", password="password"
        )

        self.u2 = get_user_model().objects.create_user(
            email="test2@example.com", password="password2"
        )

    posts = [
        Post.objects.create(
            author=self.u1,
            published_at=timezone.now(),
            title="Post 1 Title",
            slug="post-1-slug",
            summary="Post 1 Summary",
            content="Post 1 Content",
        ),
        Post.objects.create(
            author=self.u2,
            published_at=timezone.now(),
            title="Post 2 Title",
            slug="post-2-slug",
            summary="Post 2 Summary",
            content="Post 2 Content",
        ),
    ]
    # let us look up the post info by ID
    self.post_lookup = {p.id: p for p in posts}
    # override test client
    self.client = APIClient()
    token = Token.objects.create(user=self.u1)
    self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

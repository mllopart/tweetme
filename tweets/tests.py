from django.core.urlresolvers import resolve
from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.http import HttpRequest
from django.urls import reverse

from .views import TweetListView
from .models import Tweet



User = get_user_model()

def setup_view(view, request, *args, **kwargs):
    """Mimic ``as_view()``, but returns view instance.
    Use this function to get view instances on which you can run unit tests,
    by testing specific methods."""

    view.request = request
    view.args = args
    view.kwargs = kwargs
    return view

class TweetListViewTest(TestCase):

    def setUp(self):
        # self.user = UserFactory()
        self.factory = RequestFactory()

    def test_get_page_exists(self):
        request = self.factory.get(reverse('tweet:list'))
        response = TweetListView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class TweetModelTestCase(TestCase):

    def setUp(self):
        # Tweet.objects.create(
        #         user= User.objects.first(),
        #         content='some random content'
        #     )

        User.objects.create(username="UnitTestUser1")

    def test_tweet_item(self):
        obj = Tweet.objects.create(
                user= User.objects.first(),
                content='some random content'
            )

        self.assertTrue(obj.content == "some random content")
        self.assertTrue(obj.id == 1)

        absolute_url = reverse("tweet:retrieve", kwargs={"pk": obj.pk})
        self.assertEqual(obj .get_absolute_url(), absolute_url)

    def test_tweet_item_url(self):
        obj = Tweet.objects.create(
                user= User.objects.first(),
                content='some random content'
            )

        absolute_url = reverse("tweet:retrieve", kwargs={"pk": obj.pk})
        self.assertEqual(obj .get_absolute_url(), absolute_url)



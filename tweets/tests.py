from django.core.urlresolvers import resolve
from django.test import TestCase, RequestFactory
from django.http import HttpRequest
from django.urls import reverse

from .views import TweetListView



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
        request = self.factory.get(reverse('list'))
        response = TweetListView.as_view()(request)
        # if hasattr(response, 'rendered_content'):
        #     response_content = response.rendered_content
        # else:
        #     response_content = response.content

        self.assertEqual(response.status_code, 200)



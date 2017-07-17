
from .views import TweetDetailView,TweetListView
from django.conf.urls import url

urlpatterns = [
    url(r'^$',TweetListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$',TweetDetailView.as_view(), name='home'),
]


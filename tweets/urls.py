
from .views import tweet_detail_view, tweet_list_view
from django.conf.urls import url

urlpatterns = [
    url(r'^$',tweet_list_view, name='list'),
    url(r'^1/$',tweet_detail_view, name='home'),
]


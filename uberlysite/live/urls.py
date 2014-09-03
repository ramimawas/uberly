from django.conf.urls import url, include
from live import views

from live.api import TweetsResource
tweet_resource = TweetsResource()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^classify$', views.classify, name='classify'),
    url(r'^uberly', views.uberly, name='uberly'),
    url(r'^api/', include(tweet_resource.urls)),
]
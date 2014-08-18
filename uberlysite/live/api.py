"""
from tastypie.resources import ModelResource
from live.models import Entry
class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
"""

"""
class TweetResource(MongoResource):   
  class Meta:
    object_class = Tweet
    queryset = Tweet.objects.all()
    resource_name = 'tweet'
"""

#"""
from tastypie_mongoengine import resources
from live import models
class TweetsResource(resources.MongoEngineResource):
    class Meta:
        queryset = models.Tweets.objects.all().order_by('created_at')
        allowed_methods = ('get', 'post', 'put', 'patch', 'delete')
        #authorization = tastypie_authorization.Authorization()
#"""
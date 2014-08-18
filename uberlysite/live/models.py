"""
from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

class Entry(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.title)[:50]

        return super(Entry, self).save(*args, **kwargs)
"""

#"""
import mongoengine
class Tweets(mongoengine.Document):
    id = mongoengine.LongField(required=True, unique=True)
    text = mongoengine.StringField(max_length=200, required=True)
    created_at = mongoengine.DateTimeField(required=False)
#"""

"""
from mongoengine import *
class Tweet(Document):
  id = LongField(required=True)
  tweet = StringField(max_length=200, required=True)
  created_at = DateTimeField(default=datetime.datetime.now)
"""
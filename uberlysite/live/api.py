from tastypie_mongoengine import resources
import subprocess

from live import models

class TweetsResource(resources.MongoEngineResource):
    class Meta:
        queryset = models.Tweets.objects.all().order_by('created_at')
        allowed_methods = ('get', 'post', 'put', 'patch', 'delete')
        #authorization = tastypie_authorization.Authorization()

class Classifyer():
  def classify(self, tweet):
    proc = subprocess.Popen(['cd /Users/rami/github/uberly/octave && octave -q predict.m "' + tweet + '"'], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return out
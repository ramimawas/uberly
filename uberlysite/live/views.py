from django.shortcuts import render
from django.http import HttpResponse
from api import Classifyer
import json

classifyer = Classifyer()

def index(request):
  return HttpResponse("Uberly")
  
def build_response(request):
  tweet = request.GET.get('tweet')
  out = -1
  if tweet:
    out = classifyer.classify(tweet)
    msg = "%s is" % (tweet)
    msg += ' positive!' if out == '1' else ' negative!!!'
  else:
    tweet = ''
    msg = 'empty tweet'
  context = {'tweet': tweet, 'class': out, 'msg': msg}
  return context

def classify(request):
  context = build_response(request)
  return render(request, 'classify.html', context)
  
def uberly(request):
  context = build_response(request)
  if context['class'] == -1: return HttpResponse('Unauthorized', status=401)
  return HttpResponse(json.dumps(context), content_type="application/json")  
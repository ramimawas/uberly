from django.shortcuts import render
from django.http import HttpResponse
from api import Classifyer
import json

classifyer = Classifyer()

def index(request):
    return HttpResponse("Uberly")
  
def classify(request):
  print(request.GET)
  tweet = "Aggressive growth strategy for #Uber http://t.co/Bre8zukWRB by @semilshah | Boom! Exciting. http://t.co/OCtW9WBmLh"
  if 'tweet' in request.GET:
    tweet = request.GET['tweet']
  out = classifyer.classify(tweet)
  msg = tweet + '<br> is '
  if out == '1': msg += ' positive!'
  else: msg += ' negative!!'
  context = {'tweet': tweet, 'class': out, 'msg': msg}
  print context
  return render(request, 'classify.html', context)
  #return (json.dumps(context))
  
def uberly(request):
    print(request.GET)
    tweet = "Aggressive growth strategy for #Uber http://t.co/Bre8zukWRB by @semilshah | Boom! Exciting. http://t.co/OCtW9WBmLh"
    if 'tweet' in request.GET:
      tweet = request.GET['tweet']
    out = classifyer.classify(tweet)
    msg = tweet + '<br> is '
    if out == '1': msg += ' positive!'
    else: msg += ' negative!!'
    context = {'tweet': tweet, 'class': out, 'msg': msg}
    return HttpResponse(json.dumps(context), content_type="application/json")
    
  
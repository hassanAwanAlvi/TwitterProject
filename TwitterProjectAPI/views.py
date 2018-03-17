# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
import twitter
from django.shortcuts import render

api = twitter.Api(consumer_key='Lb1oVsUrltzF6tLCljXSwjg3R', consumer_secret='zNjSAOEWcPElJnunCID0EvHbQmGOt6p2fFqphSiy8b9DviCKVW',  access_token_key='376847620-wWvhGdbwewhBelJhnrruTqZuclfy6KsKLziheYSb', access_token_secret='dopDFuVvGfdkyguvSkZQ8bNmcV75sWwe7kNwojlBMjR2q')

# Create your views here.
def index(request):
    username = str(request.GET.get("username"))

    if not username:
        return HttpResponse('')
    else:
        return HttpResponse(getTweetsBasedOnUsername(username))


def retweet(request):
    id = request.GET.get("id")

    return HttpResponse(retweetID(id))

def getTweetsBasedOnUsername(username):


    t = api.GetUserTimeline(screen_name=username, count=11)
    tweets = [i.AsDict() for i in t]
    tweetsReturn = ''
    for t in tweets:
        id = ''
        try:
            id = t['retweeted_status']['id']
        except:
            id = t['id']
        tweetsReturn += t['text'] +'&p' + str(id) + '&&&'
    print tweetsReturn
    return tweetsReturn


def retweetID(tweetID):
    try:
        api.PostRetweet(tweetID)
        return 'ReTweeted successfully'
    except Exception , e:
        return e.message

from django.shortcuts import render
import os
import tweepy as tw
from django.http import HttpResponse
from django.db import models


def getParameters(request):
	tweetText = request.GET['hashtag']
	print('hello')
	print(tweetText)
	# 
	# return render(request, './templates/tweets/show.html', tweet)

	

	auth = tw.OAuthHandler('Oaa8AFy1BrFEpN217EmtNhj8D', 'fDGc7WPcSwRQgRHCNbyA59fxk7ic9JNJpCK1c3ATg1fIyu6FJW')
	auth.set_access_token('1299337287268851717-J09ZEtegD2OQT7KL2RDuiVyQXUvXdM', '2hJQytIPH0tB4ArFqIL1MzaxTjbwEm0VO3mUTx8c9Xgly')
	api = tw.API(auth, wait_on_rate_limit=True)

	search_words = "#wildfires"
	tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en").items(10)

	for tweet in tweets:
		tweetObj = Tweet(text = tweet.text)
		# print(tweet.text)

	return HttpResponse(status=200)

	#Oaa8AFy1BrFEpN217EmtNhj8D
	#fDGc7WPcSwRQgRHCNbyA59fxk7ic9JNJpCK1c3ATg1fIyu6FJW

	#1299337287268851717-J09ZEtegD2OQT7KL2RDuiVyQXUvXdM
	#2hJQytIPH0tB4ArFqIL1MzaxTjbwEm0VO3mUTx8c9Xgly
from django.shortcuts import render
import os
import tweepy as tw
from django.http import HttpResponse
from .models import Tweet
import requests
import json
from requests_oauthlib import OAuth1
from pprint import pprint




def getParameters(request):
	tag = request.GET['hashtag']
	num = request.GET['limit']

	filtered_list = fetchTweets(tag,num,request)

	return render(request, 'tweets/show.html', {'dictionary':filtered_list})

	#fetchTweets(tag, num, request)

	


def fetchTweets(tag, num, request):



	# url = "https://api.twitter.com/1.1/search/tweets.json?q="+tag+"&count="+num

	# consumer_token = 'Oaa8AFy1BrFEpN217EmtNhj8D'
	# consumer_secret = 'fDGc7WPcSwRQgRHCNbyA59fxk7ic9JNJpCK1c3ATg1fIyu6FJW'
	# access_token = '1299337287268851717-LKvQ9e3OqcmIUT12HyiqLi43ZSepd5'
	# access_secret = 'VJbnAxVAsEzLH3Up2Ot69YxPlcDNudm7fRxnC1BInawl6'

	# auth = OAuth1(consumer_token, consumer_secret,access_token, access_secret)

	# req = requests.get(url = url, auth = auth)

	# response = json.loads(req.text)
	# pprint(response)

	# for ii in response['statuses']:
 #    	pprint(response['statuses'][0]['retweeted_status']['text'])

 	#FETCHING TWEETS PART 1


	auth = tw.OAuthHandler('Oaa8AFy1BrFEpN217EmtNhj8D', 'fDGc7WPcSwRQgRHCNbyA59fxk7ic9JNJpCK1c3ATg1fIyu6FJW')
	auth.set_access_token('1299337287268851717-LKvQ9e3OqcmIUT12HyiqLi43ZSepd5', 'VJbnAxVAsEzLH3Up2Ot69YxPlcDNudm7fRxnC1BInawl6')
	api = tw.API(auth, wait_on_rate_limit=True)

	search_words = tag

	tweets = tw.Cursor(api.search,
              q=search_words,
              lang="en").items(int(num))

	print(tweets)

	for tweet in tweets:
		tweetObj = Tweet(tag = tag, text = tweet.text)		
		tweetObj.save()

	#FILTERING TWEETS PART 2 

	storedTweets = Tweet.objects.values()
	list = [entry for entry in storedTweets]

	filtered_list = []
	count = 0
	for abc in list:
		if(count == int(num)):
			break
		if(abc['tag'] == tag):
			filtered_list.append(abc)
			count = count + 1

	print(filtered_list)

	return filtered_list





	


 	

	



	#Oaa8AFy1BrFEpN217EmtNhj8D
	#fDGc7WPcSwRQgRHCNbyA59fxk7ic9JNJpCK1c3ATg1fIyu6FJW

	#1299337287268851717-J09ZEtegD2OQT7KL2RDuiVyQXUvXdM
	#2hJQytIPH0tB4ArFqIL1MzaxTjbwEm0VO3mUTx8c9Xgly

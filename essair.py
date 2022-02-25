import praw
import json
import requests
import urllib.request
import os


reddit = praw.Reddit(client_id='g6PvbFi9-f_JWC3rCJIO9A', client_secret='7xuZW9s132HfMGX0q5hwX0lF1WQwqA', user_agent='ter')

for submission in reddit.subreddit("EarthPorn").hot(limit=11):
    print(submission.url)
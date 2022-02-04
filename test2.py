import praw
import json
#from unidecode import unidecode

reddit = praw.Reddit(client_id='F2feXd56F3UXOyvpgj6SWw',client_secret='eqz3LIZsnqt7C59Ac-bh45N_mbgLZA', user_agent='sujet_19')
subreddit= reddit.subreddit('montpellier').top(limit=10)
#hots=subreddit.hot(limit=4)
dic={}
for post in subreddit:
    url=str(post.url)
    if (url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png")) :
        dic[post.id]=[post.title,post.url]

json_object = json.dumps(dic,indent = 4)
with open("sample3.json", "w") as outfile:
    outfile.write(json_object)
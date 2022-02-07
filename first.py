
import praw
import json
import requests
import urllib.request
import os



reddit = praw.Reddit(client_id='g6PvbFi9-f_JWC3rCJIO9A', client_secret='7xuZW9s132HfMGX0q5hwX0lF1WQwqA', user_agent='ter')

subreddit = reddit.subreddit("Nature")
count = 0
dic={}



    # Create directory if it doesn't exist to save images
def create_folder(image_path):
    CHECK_FOLDER = os.path.isdir(image_path)
    # If folder doesn't exist, then create it.
    if not CHECK_FOLDER:
        os.makedirs(image_path)


# Path to save images
dir_path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(dir_path, "images/")
ignore_path = os.path.join(dir_path, "ignore_images/")
create_folder(image_path)

# Iterate through top submissions
for submission in subreddit.top(limit=None):

    # Get the link of the submission
    url = str(submission.url)
    title = str(submission.title)

# Check if the link is an image
    if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):
        dic[f"image{count}"]=[title,url]
        # Retrieve the image and save it in current folder
        res=urllib.request.urlretrieve(url, f"images/image{count}.png")
        count += 1

        # Stop once you have 10 images
        if count == 10:
            break

with open('data.json', 'w') as mon_fichier:
    mon_fichier.write(json.dumps(dic, indent=4))



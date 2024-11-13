#!/usr/bin/python3
"""
Reddit API Interaction

This file will take a subreddit, fetch related data, save them to a
csv file
"""

from dotenv import load_dotenv
import datetime
import pandas as pd
import praw
import os
from tqdm import tqdm
import uuid

class Redditify:
    """
    Reddit API Interaction class
    """
    def __init__(self):
        """
        Instanstiate an instance
        """
        load_dotenv()
        user_agent = "ai-sic.myredditapp:v1.0.0. (by u/crowdpulse)"
        self.reddit = praw.Reddit(
                client_id = os.getenv("CLIENT_ID"),
                client_secret = os.getenv("CLIENT_SECRET"),
                user_agent = user_agent
                )

    def fetch_posts(self, subreddit, keyword, train):
        """
        Fetches hottest new rising top posts from a certain subreddit
        based on a keyword

        Args:
            subreddit (string): The subreddit to be searched at.
            keyword (string): The keyword to be searched about in the specific subreddit
            train (int): usually used when training the data to specify the amount of
            data to be retrieved from a specific subreddit

        Returns: None
        """
        # consider cleaning up the input and extract hot keywords from it
        self.posts = []

        try:
            if not train:
                if not keyword:
                    submissions = self.reddit.subreddit(subreddit).hot(limit=150)
                else:
                    submissions = self.reddit.subreddit(subreddit).search(keyword, limit=150)
            else:
                submissions = self.reddit.subreddit(subreddit).hot(limit=train)


            for submission in tqdm(submissions, desc="Fetching Posts", unit="post"):
                timestamp = submission.created_utc
                created_time = datetime.datetime.utcfromtimestamp(timestamp)
                post_data = {
                        'subreddit': subreddit,
                        'post_id': submission.id,
                        'post_title': submission.title,
                        'post_score': submission.score,
                        'post_url': submission.url,
                        'post_comms_num': submission.num_comments,
                        'post_body': submission.selftext,
                        'post_timestamp': created_time
                        }
                self.posts.append(post_data)
            print('The number of posts fetched from', subreddit, len(self.posts))

        except praw.exceptions as err:
            print('An error occured during retrieval of data', err)


    def pandify(self):
        """
        Converts data fetched into a csv file
        """
        if not self.posts:
            print('No data to save')
            return
        new_uuid = uuid.uuid4()
        subreddit = self.posts[0]['subreddit']
        df = pd.DataFrame(self.posts)
        df.to_csv(f"data/bert/new_{subreddit}_posts.csv", header=True, encoding='utf-8', index=False)
        #df.to_csv(f"{str(new_uuid)}_{subreddit}_posts.csv", header=True, encoding='utf-8', index=False)

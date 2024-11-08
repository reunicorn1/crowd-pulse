#!/usr/bin/python3
"""
Reddit API Interaction

This file will take a subreddit, fetch related data, save them to a
csv file
"""

from dotenv import load_dotenv
import pandas as pd
import praw
import os
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

    def fetch(self, subreddit, keyword):
        """
        Fetches hottest new rising top posts from a certain subreddit
        based on a keyword
        """
        # consider cleaning up the input and extract hot keywords from it
        self.posts = []

        try:
            if not keyword:
                # starting with a small dataset to build a database
                submissions = self.reddit.subreddit(subreddit).hot(limit=100)
                comment_limit = 10
            else:
                # This will be mostly used when with user input when making predictions
                submissions = self.reddit.subreddit(subreddit).search(keyword, limit=100)
                comment_limit = 50


            for submission in submissions:
                submission.comments.replace_more(limit=comment_limit)
                if len(submission.comments.list()) == 0:
                    continue
                for comment in submission.comments.list():
                    post_data = {
                            'Subreddit': subreddit,
                            'Post_ID': submission.id,
                            'Post_title': submission.title,
                            'Comment_text': comment.body,
                            'Comment.Score': comment.score
                            }
                    print(post_data)
                    self.posts.append(post_data)
            print('The number of comments fetched from', subreddit, len(self.posts))

        except praw.exceptions.APIException as err:
            print('An error occured during retrieval of data', err)


    def pandify(self):
        """
        Converts data fetched into a csv file
        """
        if not self.posts:
            print('No data to save')
            return
        new_uuid = uuid.uuid4()
        subreddit = self.posts[0]['Subreddit']
        df = pd.DataFrame(self.posts)
        df.to_csv(f"{str(new_uuid)}_{subreddit}_posts.csv", header=False, encoding='utf-8',
                  index=False)

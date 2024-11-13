#!/usr/bin/python3
"""
entry point
"""

from reddit import Redditify
from typing import Union
from fastapi import FastAPI
from data_cleaning import clean_csv_file
import pandas as pd

app = FastAPI()

reddit = Redditify()

@app.post("/analyze-sentiment")
def analyze_sentiment(subreddit: str , keyword: str ):
    if not subreddit and not keyword:
        return {"error": "subreddit and keyword are required"}

    reddit.fetch_posts(subreddit, keyword)
    posts_processed = clean_csv_file(data=pd.DataFrame(reddit.posts))
    return {"data": posts_processed} # TODO: add sentiment analysis


def main():
    reddit = Redditify()

    reddit.fetch_posts('solotravel', None, 2500)
    reddit.pandify()

    reddit.fetch_posts('gaming', None, 3000)
    reddit.pandify()

    reddit.fetch_posts('indiegames', None, 3000)
    reddit.pandify()

    reddit.fetch_posts('aww', None, 2000)
    reddit.pandify()

    reddit.fetch_posts('cats', None, 2000)
    reddit.pandify()

    reddit.fetch_posts('environment', None, 2500)
    reddit.pandify()

    reddit.fetch_posts('green', None, 2500)
    reddit.pandify()

    reddit.fetch_posts('science', None, 3000)
    reddit.pandify()

    reddit.fetch_posts('space', None, 3000)
    reddit.pandify()

    reddit.fetch_posts('nba', None, 2500)
    reddit.pandify()

    reddit.fetch_posts('soccer', None, 2500)
    reddit.pandify()

    reddit.fetch_posts('history', None, 2500)
    reddit.pandify()

    reddit.fetch_posts('Philosophy', None, 2500)
    reddit.pandify()
if __name__ == '__main__':
    main()

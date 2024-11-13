#!/usr/bin/python3
"""
entry point
"""

from reddit import Redditify

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

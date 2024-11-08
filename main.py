#!/usr/bin/python3
"""
entry point
"""

from reddit import Redditify

def main():
    reddit = Redditify()
    reddit.fetch('AskReddit', None)
    reddit.pandify()

if __name__ == '__main__':
    main()

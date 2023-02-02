#!/usr/bin/python3
"""returns the number of subscribers (not active users,
total subscribers) for a given subreddit"""

import requests
import sys
after = None
count_dict = []


def count_words(subreddit, word_list):
    """returns the number of subscribers"""
    global after
    global count_dict
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Spam4Karma'}
    param = {'after': after}
    res = requests.get(url, headers=headers, allow_redirects=False,
                       params=param)

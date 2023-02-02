#!/usr/bin/python3
"""returns the number of subscribers (not active users,
total subscribers) for a given subreddit"""

import requests
import sys


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Spam4Karma'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        return (res.json().get("data").get("subscribers"))
    return (0)

#!/usr/bin/python3
"""returns the number of subscribers (not active users,
total subscribers) for a given subreddit"""

import requests
import sys


def top_ten(subreddit):
    """returns the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Spam4Karma'}
    param = {'limit': 10}
    res = requests.get(url, headers=headers, allow_redirects=False,
                        params=param)
    if res.status_code == 200:
        tittles = res.json().get("data").get("children")
        for tittle in tittles:
            print(tittle.get('data').get('title'))
    else:
        print(None)

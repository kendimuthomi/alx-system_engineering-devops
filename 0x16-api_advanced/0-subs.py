#!/usr/bin/python3
"""returns the number of subscribers (not active users,
total subscribers) for a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'kendimuthomi'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        return (res.json().get("data").get("subscribers"))

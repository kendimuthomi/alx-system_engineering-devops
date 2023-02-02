#!/usr/bin/python3
"""returns the number of subscribers (not active users,
total subscribers) for a given subreddit"""

import requests

def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    req = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                        headers={'User-Agent': 'kendimuthomi'}, allow_redirects=False)
    if req.status_code == 200:
        return req.json().get("data").get("subscribers")

#!/usr/bin/python3
"""returns the number of subscribers (not active users,
total subscribers) for a given subreddit"""

import requests
import sys
after=None


def recurse(subreddit, hot_list=[]):
    """returns the number of subscribers"""
    global after
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Spam4Karma'}
    param = {'after': after}
    res = requests.get(url, headers=headers, allow_redirects=False,
                       params=param)
    if res.status_code == 200:
        next_ = res.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        tittles = res.json().get("data").get("children")
        for tittle in tittles:
            hot_list.append(tittle.get('data').get('title'))
        return hot_list
    else:
        return (None)

#!/usr/bin/python3
"""returns a list of titles of all hot posts
in a subreddit. """
import requests
from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list of titles of all hot posts
    in a subreddit.
    """
    url = ('http://www.reddit.com/r/{}/hot.json?limit=100'
           '&&after={}').format(subreddit, after)
    header = {'User-Agent': 'MyBot'}

    try:
        response = get(url, headers=header)

        reddit_data = response.json()
        dict_len = len(reddit_data['data']['children'])
        for i in range(dict_len):
            hot_list.append(reddit_data['data']['children'][i]
                            ['data']['title'])
        after = reddit_data['data']['after']

        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except requests.exceptions.RequestException as e:
        return None

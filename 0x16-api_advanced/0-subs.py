#!/usr/bin/python3
"""returns numder of subscripres in a given subreddit."""
import requests
from requests import get


def number_of_subscribers(subreddit):
    """returns numder of subscripres in a given subreddit."""
    url = f'http://www.reddit.com/r/{subreddit}/about.json'
    header = {"User-Agent": "Mybot"}
    response = get(url, headers=header)

    try:
        subreddit_data = response.json()
        return subreddit_data['data']['subscribers']
    except:
        return 0

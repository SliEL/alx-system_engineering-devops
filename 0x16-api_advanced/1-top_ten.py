#!/usr/bin/python3
"""
prints top 10 hot post 
titles in a subreddit.
"""
from requests import get


def top_ten(subreddit):
    """Prints top 10 hot posts in a subreddit."""
    url = f"http://www.reddit.com/r/{subreddit}/hot.json"
    header = {'User-Agent': 'Mybot'}
    response = get(url, headers=header)
    try:
        reddit_data = response.json()
        for i in range(10):
            print(reddit_data['data']['children'][i]['data']['title'])
    except:
        print(None)

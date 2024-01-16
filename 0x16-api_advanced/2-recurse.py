#!/usr/bin/python3
"""returns a list of titles of all hot posts
in a subreddit. """

from requests import get

def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list of titles of all hot posts
    in a subreddit.
    """
    url = f'http://www.reddit.com/r/{subreddit}/hot.json?limit=100&&after={after}'
    header = {'User-Agent': 'MyBot'}
    try:
        response = get(url, headers=header)

        reddit_data = response.json()
        dict_len = len(reddit_data['data']['children'])
        for i in range(dict_len):
            hot_list.append(reddit_data['data']['children'][i]['data']['title'])
        
        after = reddit_data['data']['after']

        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except:
        return None

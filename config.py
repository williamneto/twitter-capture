#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module sets user credentials for Twitter collecting
and streaming, as well as the API URL for sending tweets.

The APP_KEYS var is imported for collecting already published
tweets, while the vars APP_KEY, APP_SECRET, OAUTH_TOKEN and
OAUTH_TOKEN_SECRET are imported for streaming live tweets.

The POST_URL var is used for sending the obtained tweets over
to an external API endpoint, and becomes the default if set.
However, if another URL is given on execution time with the
"--url" argument, the former will be ignored for the latter.
"""

APP_KEYS = [ 
	['UFnObKlRXS8SzHST8qYX2SJZw', 'mgUcSX2oh3ME67yc9uU0FjtdWWOwqGZDl7Y1O9l6Ez3YZcI1dp']
]

APP_KEY = 'UFnObKlRXS8SzHST8qYX2SJZw'
APP_SECRET = 'mgUcSX2oh3ME67yc9uU0FjtdWWOwqGZDl7Y1O9l6Ez3YZcI1dp'
OAUTH_TOKEN = '920756820590891008-kAPdt2RHzqis6k27aQ60mtYlCIKlRcF'
OAUTH_TOKEN_SECRET = '7sUwX6PKQSQwZ62vhUEhLXGn5NvXaBUWQOjYZFYeJyxAs'

POST_URL = 'http://127.0.0.1:5000/receive_tweets'

# LOG_OUTPUT = False # default: True
# STREAM_RTS = False # retweets, default: True
# STREAM_ATS = False # @-messages, default: True
# -*- coding utf-8 -*-
import json
import pytz
from dateutil import parser
from datetime import datetime

from app.models import User, Tweet
from tweetsreader import settings

class ImportFromJson(object):
    def __init__(self, filename, tag, *args, **kwargs):
        self.tag = tag
        self.filename = filename
    
    def str_to_date(self, str):
        obj = parser.parse(str)
        local_tz = pytz.timezone("America/Sao_Paulo")
        local_dt = obj.replace(tzinfo=pytz.utc).astimezone(local_tz)

        return local_dt

    def save_tweet(self, tweet):
        if len(User.objects.all().filter(id_str=tweet["user"]["id_str"])) == 0:
            user_obj = User()
            user_obj.id_str = tweet["user"]["id_str"]
            user_obj.name = tweet["user"]["name"]
            user_obj.screen_name = tweet["user"]["screen_name"]
            user_obj.location = tweet["user"]["location"]
            user_obj.url = tweet["user"]["url"]
            user_obj.description = tweet["user"]["description"]
            user_obj.verified = tweet["user"]["verified"]
            user_obj.follower = tweet["user"]["followers_count"]
            user_obj.statuses_count = tweet["user"]["statuses_count"]
            user_obj.created_at = self.str_to_date(tweet["user"]["created_at"])
            user_obj.profile_image_url = tweet["user"]["profile_image_url"]
            user_obj.save()

            user = user_obj
        else:
            user = User.objects.all().filter(id_str=tweet["user"]["id_str"])[0]
        
        if len(Tweet.objects.all().filter(id_str=tweet["id_str"])) == 0:
            tweet_obj = Tweet()
            tweet_obj.id_str = tweet["id_str"]
            tweet_obj.credated_at = self.str_to_date(tweet["created_at"])
            tweet_obj.tag = self.tag
            tweet_obj.user = user
            tweet_obj.text = tweet["text"]
            tweet_obj.in_reply_to_status_id = tweet["in_reply_to_status_id"]
            tweet_obj.in_reply_to_user_id = tweet["in_reply_to_user_id"]
            tweet_obj.in_reply_to_screen_name = tweet["in_reply_to_screen_name"]
            tweet_obj.geo = tweet["geo"]
            tweet_obj.coordinates = tweet["coordinates"]
            tweet_obj.place = tweet["place"]

            if tweet["is_quote_status"]:
                if  len(Tweet.objects.all().filter(id_str=tweet["quoted_status"]["id_str"])) == 0:
                    if len(User.objects.all().filter(id_str=tweet["quoted_status"]["user"]["id_str"])) == 0:
                        quoted_user_obj = User()
                        quoted_user_obj.id_str = tweet["quoted_status"]["user"]["id_str"]
                        quoted_user_obj.name = tweet["quoted_status"]["user"]["name"]
                        quoted_user_obj.screen_name = tweet["quoted_status"]["user"]["screen_name"]
                        quoted_user_obj.location = tweet["quoted_status"]["user"]["location"]
                        quoted_user_obj.url = tweet["quoted_status"]["user"]["url"]
                        quoted_user_obj.description = tweet["quoted_status"]["user"]["description"]
                        quoted_user_obj.verified = tweet["quoted_status"]["user"]["verified"]
                        quoted_user_obj.follower = tweet["quoted_status"]["user"]["followers_count"]
                        quoted_user_obj.statuses_count = tweet["quoted_status"]["user"]["statuses_count"]
                        quoted_user_obj.created_at = self.str_to_date(tweet["quoted_status"]["user"]["created_at"])
                        quoted_user_obj.profile_image_url = tweet["quoted_status"]["user"]["profile_image_url"]
                        quoted_user_obj.save()
                    else:
                        quoted_user_obj = User.objects.all().filter(id_str=tweet["user"]["id_str"])[0]
                    
                    quoted_obj = Tweet()
                    quoted_obj.id_str = tweet["id_str"]
                    quoted_obj.credated_at = self.str_to_date(tweet["quoted_status"]["created_at"])
                    quoted_obj.user = quoted_user_obj
                    quoted_obj.tag = self.tag
                    quoted_obj.text = tweet["quoted_status"]["text"]
                    quoted_obj.in_reply_to_status_id = tweet["quoted_status"]["in_reply_to_status_id"]
                    quoted_obj.in_reply_to_user_id = tweet["quoted_status"]["in_reply_to_user_id"]
                    quoted_obj.in_reply_to_screen_name = tweet["quoted_status"]["in_reply_to_screen_name"]
                    quoted_obj.geo = tweet["quoted_status"]["geo"]
                    quoted_obj.coordinates = tweet["quoted_status"]["coordinates"]
                    quoted_obj.place = tweet["quoted_status"]["place"]
                    quoted_obj.quote_count = tweet["quoted_status"]["quote_count"]
                    quoted_obj.reply_count = tweet["quoted_status"]["reply_count"]
                    quoted_obj.retweet_count = tweet["quoted_status"]["retweet_count"]
                    quoted_obj.favorite_count = tweet["quoted_status"]["favorite_count"]
                    quoted_obj.entities = tweet["quoted_status"]["entities"]
                    quoted_obj.save()
                else:
                    quoted_obj = Tweet.objects.all().filter(id_str=tweet["quoted_status"]["id_str"])[0]
                
                tweet_obj.quoted_status_id = tweet["quoted_status_id_str"]
                tweet_obj.is_quote_status = tweet["is_quote_status"]
                tweet_obj.quoted_status = quoted_obj
                tweet_obj.quoted_status_permalink = tweet["quoted_status_permalink"]["url"]
                tweet_obj.quoted_status_id = tweet["quoted_status_id"]
            
            tweet_obj.quote_count = tweet["quote_count"]
            tweet_obj.reply_count = tweet["reply_count"]
            tweet_obj.retweet_count = tweet["retweet_count"]
            tweet_obj.favorite_count = tweet["favorite_count"]
            tweet_obj.entities = tweet["entities"]
            tweet_obj.save()

            return tweet_obj

    def start(self, to_load):
        response = "null"
        with open(self.filename) as file:
            tweets = json.load(file)
            if to_load == "all":
                for t in tweets:
                    response = self.save_tweet(t)
            elif isinstance(to_load, int):
                response = self.save_tweet(tweets[to_load])
        
        return response

        
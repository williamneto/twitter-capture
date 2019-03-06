# -*- coding: utf-8 -*-
from datetime import timedelta

from app.models import Tweet, User

class TimeLineGraph(object):
    def __init__(self, *args, tags, **kwargs):
        self.tags = tags
        self.num_tags = len(tags)
    
    def get_tag_data(self, tag):
        tweets = Tweet.objects.all().filter(tag=tag)
        return tweets
    
    def generate_graph_data(self):
        if self.num_tags == 1:
            tweets = self.get_tag_data(self.tags[0])
            num_tweets = len(tweets)

            start_time = tweets[0].created_at
            end_time = tweets[num_tweets-1].created_at
            tdelta = end_time - start_time
            minutes = (tdelta.seconds-0*60*60)//60

            labels = []
            values = []
            for m in range(1, minutes, 10):
                query = tweets.filter(
                    created_at__gte=start_time + timedelta(seconds=(m-1)*60),
                    created_at__lte=start_time + timedelta(seconds=m*60)
                )
                dtime = start_time + timedelta(seconds=m*60)
                labels.append(dtime.strftime("%H:%M:%S"))
                values.append(len(query))
            
            data = {
                "labels": labels,
                "values": values
            }
        elif self.num_tags == 2:
            queryes = []
            for tag in self.tags:
                queryes.append(
                    Tweet.objects.all().filter(tag=tag)
                )
            
            tweets = queryes[0].union(queryes[1]).order_by("created_at")
            num_tweets = len(tweets)

            start_time = tweets[0].created_at
            end_time = tweets[num_tweets-1].created_at
            tdelta = end_time - start_time
            minutes = (tdelta.seconds-0*60*60)//60
            #import pdb; pdb.set_trace()
            print(">>>>>>>>"+str(minutes))

            labels = []
            values = []
            #import pdb; pdb.set_trace()
            for m in range(1, minutes, 10):
                print(m)
                query = tweets.filter(
                    created_at__gte=start_time + timedelta(seconds=(m-1)*60),
                    created_at__lte=start_time + timedelta(seconds=m*60)   
                )
                dtime = start_time + timedelta(seconds=m*60)
                labels.append(dtime.strftime("%H:%M:%S"))
                values.append(len(query))

            data = {
                "labels": labels,
                "values": values
            }

        
        return data





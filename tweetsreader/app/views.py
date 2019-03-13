# -*- coding: utf-8 -*-
import json
from pytz import timezone
from django.views.generic import TemplateView
from django.http import JsonResponse

from app.operations import TimeLineGraph
from app.models import Tag, Tweet

class ViewTags(TemplateView):
    template_name = "tags_view.html"
    get_services = ("get_timeline_graph",)

    def get(self, *args, **kwargs):
        cmd = self.request.GET.get("cmd")
        if cmd and cmd in self.get_services:
            return getattr(self, "_%s" % cmd)()
        
        return super(ViewTags, self).get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        ctx = super(ViewTags, self).get_context_data(*args, **kwargs)
        tags = Tag.objects.all().filter()
        tag = self.request.GET.get("tag")

        all_tags_names = []
        for t in tags:
            if not t.name == tag:
                all_tags_names.append(t.name)
        
        tweets_for_tag = Tweet.objects.all().filter(
            tag=tag
        ).order_by("created_at")
        end_time = tweets_for_tag[len(tweets_for_tag)-1].created_at
        start_time = tweets_for_tag[0].created_at
        
        ctx["start_time"] = start_time.astimezone(timezone("America/Sao_Paulo"))
        ctx["end_time"] = end_time.astimezone(timezone("America/Sao_Paulo"))
        ctx["tweets_for_tag"] = len(tweets_for_tag)
        ctx["all_tags_names"] = all_tags_names
        ctx["tag"] = tag

        return ctx
    
    def _get_timeline_graph(self):
        tags = [x.strip() for x in self.request.GET.get("tag").split(",")]
        tlg = TimeLineGraph(tags=tags)

        graph_data = tlg.generate_graph_data()

        return JsonResponse(graph_data, safe=False)



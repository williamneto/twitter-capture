# -*- coding: utf-8 -*-
import json
from django.views.generic import TemplateView
from django.http import JsonResponse

from app.operations import TimeLineGraph

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
        ctx["tags"] = self.request.GET.get("tags")

        return ctx
    
    def _get_timeline_graph(self):
        tags = [x.strip() for x in self.request.GET.get("tags").split(",")]
        tlg = TimeLineGraph(tags=tags)

        graph_data = tlg.generate_graph_data()

        return JsonResponse(graph_data, safe=False)



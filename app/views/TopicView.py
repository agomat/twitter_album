from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from app.views.mixins.CommonListsMixin import CommonListsMixin
from app.models import Album, Photo


class TopicView(CommonListsMixin, ListView):
    model = Photo
    context_object_name = "images"
    template_name = "app/sections/index.html"

    def get_queryset(self):
        active_topic = get_object_or_404(Album, topic_name=self.kwargs['topic'])
        return Photo.objects.filter(album=active_topic)

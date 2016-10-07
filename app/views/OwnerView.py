from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from app.views.mixins.CommonListsMixin import CommonListsMixin
from app.models import Album, Photo, Owner


class OwnerView(CommonListsMixin, ListView):
    model = Photo
    context_object_name = "images"
    template_name = "app/sections/index.html"

    def get_queryset(self):
        owner = get_object_or_404(Owner, screen_name=self.kwargs['owner'])
        return Photo.objects.filter(owner=owner)

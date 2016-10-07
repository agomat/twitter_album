from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from app.views.mixins.CommonListsMixin import CommonListsMixin
from app.models import Photo, Owner
from django.http import HttpResponse
import json


class OwnerView(CommonListsMixin, ListView):
    model = Photo
    context_object_name = "images"
    template_name = "app/sections/index.html"

    def get_queryset(self):
        owner = get_object_or_404(Owner, screen_name=self.kwargs['owner'])
        return Photo.objects.filter(owner=owner)

    def dispatch(self, request, *args, **kwargs):
        # Check if the client is asking for an API
        # before dispatching to view-templete as usual
        if request.get_full_path().startswith('/api'):
            result = self.get_queryset()
            dictionaries = [obj.as_dict() for obj in result]
            return HttpResponse(json.dumps({"data": dictionaries}), content_type='application/json')

        return super(OwnerView, self).dispatch(request, *args, **kwargs)

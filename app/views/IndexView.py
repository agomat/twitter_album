from django.views.generic import TemplateView
from app.views.mixins.CommonListsMixin import CommonListsMixin
from django.http import HttpResponse
from app.models import Photo
import json


class IndexView(CommonListsMixin, TemplateView):
    template_name = "app/sections/index.html"

    def dispatch(self, request, *args, **kwargs):
        # Check if the client is asking for an API
        # before dispatching to view-templete as usual
        if request.get_full_path().startswith('/api'):
            dictionaries = [obj.as_dict() for obj in Photo.objects.all()]
            return HttpResponse(json.dumps({"data": dictionaries}), content_type='application/json')

        return super(IndexView, self).dispatch(request, *args, **kwargs)

from django.views.generic import TemplateView
from app.views.mixins.CommonListsMixin import CommonListsMixin


class IndexView(CommonListsMixin, TemplateView):
    template_name = "app/sections/index.html"

    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)

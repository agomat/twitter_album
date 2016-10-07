from django.views.generic.base import ContextMixin
from app.models import Owner, Album, Photo


class CommonListsMixin(ContextMixin):

    def get_topics(self):
        return Album.objects.all()

    def get_owners(self):
        return Owner.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CommonListsMixin, self).get_context_data(**kwargs)
        context['topics'] = self.get_topics()
        context['owners'] = self.get_owners()
        return context
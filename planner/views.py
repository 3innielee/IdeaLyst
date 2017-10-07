from django.shortcuts import render
from . import models
from django.views.generic import TemplateView
from datetime import datetime, timedelta

# Create your views here.
class DayView(TemplateView):
    template_name = 'planner/day.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if self.kwargs.get('pk'):
            pk = self.kwargs.get('pk')
            date = datetime(year=int(pk[0:4]), month=int(pk[4:6]), day=int(pk[6:8]))
            yesterday = date - timedelta(days=1)
            tmrw = date + timedelta(days=1)
            context['valid'] = True
            context['yesterday'] = yesterday.strftime("%Y%m%d")
            context['tmrw'] = tmrw.strftime("%Y%m%d")
            context['day'] = date.strftime('%m-%d-%Y')
            context['events'] = models.Event.objects.filter(author=self.request.user, day=date)
        else:
            context['valid'] = False

        return context

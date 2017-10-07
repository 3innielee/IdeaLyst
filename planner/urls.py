from django.conf.urls import url
from . import views

app_name = 'planner'

urlpatterns = [
    url(r'^day/(?P<pk>[\w.@+-]+)$', view=views.DayView.as_view(), name='day'),
    url(r'^new/$', view=views.EventCreateView.as_view(), name='new_event')
]

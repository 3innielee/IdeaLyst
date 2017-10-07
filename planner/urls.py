from django.conf.urls import url
from . import views

app_name = 'planner'

urlpatterns = [
    url(r'^(?P<pk>[\w.@+-]+)$', view=views.DayView.as_view(), name='day')
]

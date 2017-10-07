from django.contrib import admin
from .models import Location
from .models import Event

# Register your models here.
admin.site.register(Location)
admin.site.register(Event)

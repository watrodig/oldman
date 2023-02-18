from django.contrib import admin
from api.models import *

class EventAdmin(admin.ModelAdmin):
    list_display = ('name',)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Event, EventAdmin)
admin.site.register(EventCategory, EventCategoryAdmin)
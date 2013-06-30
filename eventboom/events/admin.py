from django.contrib import admin

from models import Event, UserProfile

class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "datetime", "neighborhood")
    search_fields = ("title", "datetime", "location", "creator")
admin.site.register(Event, EventAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("display_name", "email", "phone")
    search_fields = ["display_name", "email", "phone"]
admin.site.register(UserProfile, UserProfileAdmin)


from django.contrib import admin

from app.models import User,Tweet, Tag

admin.site.register(User)
admin.site.register(Tweet)
admin.site.register(Tag)

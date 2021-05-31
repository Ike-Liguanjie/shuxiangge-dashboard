from django.contrib import admin

from .models import User, Favorite

admin.site.register(User)
admin.site.register(Favorite)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportModelAdmin

from .models import User, Favorite, ReadLog
from .resource import UserResources


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('gender', 'phone', 'email', 'qq')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'phone', 'last_login', 'is_active')
    search_fields = ('username', 'phone')
    list_filter = ('last_login', 'is_active')
    resource_class = UserResources


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    fields = ('user_id', 'book_id', 'created_time')
    list_filter = ('user_id', 'book_id', 'created_time')


@admin.register(ReadLog)
class ReadLogAdmin(admin.ModelAdmin):
    fields = ('user_id', 'book_id', 'created_time')
    list_filter = ('user_id', 'book_id', 'created_time')

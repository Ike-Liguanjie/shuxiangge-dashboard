from django.db import models
from django.contrib import admin
from django.utils.timezone import now
from datetime import datetime


class BaseModel(models.Model):
    created_by = models.CharField(max_length=10, verbose_name=u"创建人")
    created_time = models.DateTimeField(default=now, verbose_name=u"创建日期")
    updated_by = models.CharField(max_length=10, verbose_name=u"修改人")
    updated_time = models.DateTimeField(default=now, verbose_name=u"更新日期")

    class Meta:
        abstract = True


class BaseAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user.username
            obj.updated_by = request.user.username
        else:
            obj.updated_by = request.user.username
            obj.updated_time = datetime.now()
        super(BaseAdmin, self).save_model(request, obj, form, change)

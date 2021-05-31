from django.db import models
from django.utils.timezone import now
from datetime import datetime


class BaseModel(models.Model):
    created_by = models.CharField(max_length=10, verbose_name=u"创建人")
    created_time = models.DateTimeField(default=now, verbose_name=u"创建日期")
    updated_by = models.CharField(max_length=10, verbose_name=u"修改人")
    updated_time = models.DateTimeField(default=now, verbose_name=u"更新日期")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updated_time = datetime.now()
        return super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True

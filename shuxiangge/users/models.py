from django.contrib.auth.models import AbstractUser as DjangoUser
from ..books.models import Book, BaseModel, models

GENDER = (
    (1, u"男"),
    (2, u"女"),
)


class User(DjangoUser):
    phone = models.CharField(max_length=11, blank=True, null=True, verbose_name=u"手机号")
    gender = models.SmallIntegerField(blank=True, null=True, choices=GENDER, verbose_name=u"性别")
    qq = models.CharField(blank=True, null=True, max_length=12, verbose_name=u"qq")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = u"用户管理"
        verbose_name_plural = verbose_name


class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"收藏人")
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name=u"收藏书籍")
    created_time = models.DateTimeField(verbose_name=u"收藏时间")

    class Meta:
        verbose_name = u"收藏管理"
        verbose_name_plural = verbose_name


class ReadLog(models.Model):
    user_id = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=u"用户名")
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name=u"小说名")
    created_time = models.DateTimeField(verbose_name=u"记录时间")

    class Meta:
        verbose_name = u"阅读记录"
        verbose_name_plural = verbose_name

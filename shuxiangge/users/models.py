from ..books.models import Book, BaseModel, models

SEX = (
    (1, u"男"),
    (2, u"女"),
)


class User(BaseModel):
    account = models.CharField(max_length=32, null=False, verbose_name=u"账户名")
    password = models.CharField(max_length=128, null=False, verbose_name=u"密码")
    email = models.CharField(max_length=64, null=False, verbose_name=u"邮箱")
    phone = models.IntegerField(null=False, verbose_name=u"手机号")
    sex = models.SmallIntegerField(null=False, choices=SEX, verbose_name=u"性别")
    qq = models.CharField(max_length=32, null=False, verbose_name=u"qq")

    def __str__(self):
        return self.account

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

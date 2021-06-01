from ..utils.base import models, BaseModel

BOOK_STATUS = (
    (0, u"下架"),
    (1, u"连载"),
    (2, u"完本"),
)


class Category(BaseModel):
    name = models.CharField(max_length=50, null=False, verbose_name=u"分类名称")
    order = models.IntegerField(default=0, verbose_name=u"展示顺序")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"小说分类"
        verbose_name_plural = verbose_name
        ordering = ("order",)


class Book(BaseModel):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name=u"所属分类")
    name = models.CharField(max_length=128, verbose_name=u"小说名称")
    author = models.CharField(max_length=32, verbose_name=u"作者")
    introduction = models.CharField(max_length=512, verbose_name=u"简介")
    lasted_chapter = models.ForeignKey("Chapter", db_column="lasted_chapter", on_delete=models.SET_NULL,
                                       null=True, verbose_name=u"最新章节")
    favorites_nums = models.IntegerField(default=0, null=False, verbose_name=u"收藏数")
    status = models.SmallIntegerField(null=False, choices=BOOK_STATUS, verbose_name="状态")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"小说管理"
        verbose_name_plural = verbose_name
        ordering = ("id",)


class Chapter(BaseModel):
    book_id = models.ForeignKey(Book, db_column="book_id", on_delete=models.CASCADE, verbose_name=u"书籍ID")
    name = models.CharField(max_length=64, null=False, verbose_name=u"章节名称")
    content_url = models.CharField(max_length=64, verbose_name=u"章节路径")
    index = models.IntegerField(default=0, null=False, verbose_name=u"章节索引")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"小说章节"
        verbose_name_plural = verbose_name
        ordering = ("book_id",)

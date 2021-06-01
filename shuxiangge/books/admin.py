from ..utils.base import admin, BaseAdmin

from .models import Book, Category, Chapter


@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    fields = ('name', 'order')
    list_display = ('name', 'order')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(BaseAdmin):
    fields = ('category_id', 'name', 'author', 'introduction', 'lasted_chapter', 'updated_time', 'favorites_nums',
              'status')
    list_display = ('category_id', 'name', 'author', 'introduction', 'lasted_chapter', 'updated_time', 'favorites_nums',
                    'status')
    search_fields = ('name', 'author')
    list_filter = ('category_id', 'status', 'updated_time')


@admin.register(Chapter)
class ChapterAdmin(BaseAdmin):
    fields = ('book_id', 'name', 'content_url', 'index')
    list_display = ('book_id', 'name', 'content_url', 'index')
    search_fields = ('name',)
    list_filter = ('book_id',)

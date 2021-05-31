from django.contrib import admin

from .models import Book, Category, Chapter

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Chapter)


admin.site.site_title = '书香阁管理后台'
admin.site.site_header = '书香阁管理后台'
admin.site.index_title = '书香阁管理后台'

from django.contrib import admin
from books.models import BookModel
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'author', 'email', 'describe']


admin.site.register(BookModel, BookAdmin)
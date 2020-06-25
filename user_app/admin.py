from django.contrib import admin
from user_app.models import BookInfo

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'bpub_date']

admin.site.register(BookInfo, BookInfoAdmin)
from django.contrib import admin
from .models import News, Category




class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    save_on_top = True


admin.site.register(News, NewsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')  

admin.site.register(Category, CategoryAdmin)
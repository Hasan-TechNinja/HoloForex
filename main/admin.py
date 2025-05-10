from django.contrib import admin
from . models import About, Blog, Category, Comment

# Register your models here.

class AboutModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'name', 'about', 'about_image', 'mission', 'mission_image', 'vision', 'we_offer', 'why_choose', 'choose_image'
    )
admin.site.register(About, AboutModelAdmin)

class BlogModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'title', 'image', 'category', 'description', 'date', 'view'
    )
admin.site.register(Blog, BlogModelAdmin)


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'name', 'description', 'image'
    )
admin.site.register(Category, CategoryModelAdmin)


class CommentModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'blog', 'comment'
    )
admin.site.register(Comment, CommentModelAdmin)
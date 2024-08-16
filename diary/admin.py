from django.contrib import admin

from diary.models import BlogPost, About


# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ["title", "date_posted", "date_updated"]
    search_fields = ('title', 'content')

admin.site.register(BlogPost, BlogPostAdmin)

class AboutAdmin(admin.ModelAdmin):
    pass

admin.site.register(About, AboutAdmin)
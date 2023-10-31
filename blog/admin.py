from django.contrib import admin

from blog.models import Post


# customize the blog admin page
class BlogAdmin(admin.ModelAdmin[Post]):
    list_display = (
        "id",
        "episode_number",
        "content",
        "created_at",
        "updated_at",
    )
    list_display_links = ("id", "episode_number")
    search_fields = ("episode_number",)
    list_per_page = 10


admin.site.register(Post, BlogAdmin)

from django.contrib import admin
from .models import *

#admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'publish', 'status', 'author']
    ordering = ["publish"]
    list_filter = ['status', 'author', 'publish']
    search_fields = ['title', 'description']
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug': ['title']}
    list_editable = ['status']
    # list_display_links = ['author']
    # autocomplete_fields = ['author']

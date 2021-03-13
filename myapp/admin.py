from django.contrib import admin
from .models import Blog
# pip install django-import-export
from import_export.admin import ImportExportModelAdmin

class BlogAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ['id', 'author', 'title', 'dop', 'banner']
	list_editable = ['title', 'banner']
	ordering = ['-title']
	list_filter = ['dop']
	search_fields = ['title', 'author']
	list_per_page = 1

admin.site.register(Blog, BlogAdmin)


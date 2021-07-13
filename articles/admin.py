from django.contrib import admin
from . import models

admin.site.register(models.Article)


@admin.register(models.Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', "body", 'article', 'date', 'active')
    list_filter = ('active', 'date')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(models.Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', "body", 'article', 'date', 'active')
    list_filter = ('active', 'date')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

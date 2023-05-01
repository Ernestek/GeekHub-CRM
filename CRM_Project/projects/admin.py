from django.contrib import admin

from projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner',)
    list_display_links = ('id', 'name',)
    readonly_fields = ('created_at', 'updated_at',)
# Register your models here.

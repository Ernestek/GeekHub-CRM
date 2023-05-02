from django.contrib import admin

from projects.forms import ProjectForm
from projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm

    list_display = ('id', 'name', 'owner',)
    list_display_links = ('id', 'name',)
    readonly_fields = ('created_at', 'updated_at',)

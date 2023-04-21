from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from tasks.models import UserTask


@admin.register(UserTask)
class UserTaskAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'user',)
    list_display_links = ('id', 'title',)

    list_filter = ('user', )
    fieldsets = (
        (None, {'fields': ('title', 'text')}),
        (_('User info'), {'fields': ('user', 'user_assigned',)}),
        (_('Task info'), {'fields': ('status',)}),
    )



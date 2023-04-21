from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from django.utils.translation import gettext_lazy as _

from account.forms import UserCreateForm
from account.models import User


@admin.register(User)
class UserAdmin(_UserAdmin):
    add_form = UserCreateForm
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff',)
    list_display_links = ('id', 'email',)
    list_filter = ('first_name', 'last_name', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone_number',
                                         'phone_number2', 'phone_number3',)}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_active',
                                       'is_staff', 'password_changed',
                                       )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',)}
         ),
    )
    search_fields = ('email', 'first_name', 'last_name', )
    ordering = ('email',)
    filter_horizontal = ()

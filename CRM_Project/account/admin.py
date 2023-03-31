from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import UserCreateForm
from .models import User


@admin.register(User)
class UserAdmin(_UserAdmin):
    add_form = UserCreateForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff',)
    list_filter = ('first_name', 'last_name', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone_number',)}),
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

    # def save_model(self, request, obj, form, change):
    #     print(request)
    #     password = User.objects.make_random_password()
    #     super(UserAdmin, self).save_model(request, obj, form, change)
    #     print(password)
    #     obj.set_password(password)
    #     # message_for_registered_user(
    #     #     obj, password, '123'
    #     # )

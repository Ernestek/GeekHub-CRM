from django.contrib import admin
from django.forms import inlineformset_factory

from partners.models import Partner, PartnerContactPerson


class PartnerContactPersonInline(admin.TabularInline):
    model = PartnerContactPerson
    extra = 1


@admin.register(Partner)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    inlines = [PartnerContactPersonInline]

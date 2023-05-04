from django.contrib import admin

from partners.models import Partner, PartnerContactPerson


class PartnerContactPersonInline(admin.TabularInline):
    model = PartnerContactPerson
    extra = 1
    readonly_fields = ('id', )


@admin.register(Partner)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    inlines = [PartnerContactPersonInline,]



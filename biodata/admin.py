from django.contrib import admin
from .models import (
    PersonalInfo, Education, Property, CareerEntry,
    FamilyMember, FamilyMemberTag, LineageNode,
    HeritageInfo, MoolCard, GalleryImage, Greeting, NavLink
)


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'role_title', 'current_company']

    def has_add_permission(self, request):
        return not PersonalInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'year_range', 'order']
    list_editable = ['order']


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']


@admin.register(CareerEntry)
class CareerEntryAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'role', 'is_current', 'order']
    list_editable = ['order', 'is_current']


class FamilyMemberTagInline(admin.TabularInline):
    model = FamilyMemberTag
    extra = 1


@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'relation', 'order']
    list_editable = ['order']
    inlines = [FamilyMemberTagInline]


@admin.register(LineageNode)
class LineageNodeAdmin(admin.ModelAdmin):
    list_display = ['name_hindi', 'name_english', 'role_label', 'is_self', 'order']
    list_editable = ['order']


@admin.register(HeritageInfo)
class HeritageInfoAdmin(admin.ModelAdmin):
    list_display = ['gotra_hindi', 'gotra_english']

    def has_add_permission(self, request):
        return not HeritageInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(MoolCard)
class MoolCardAdmin(admin.ModelAdmin):
    list_display = ['label_hindi', 'order']
    list_editable = ['order']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['alt_text', 'category', 'is_featured', 'order']
    list_editable = ['order', 'is_featured']


@admin.register(Greeting)
class GreetingAdmin(admin.ModelAdmin):
    list_display = ['text', 'order']
    list_editable = ['order']


@admin.register(NavLink)
class NavLinkAdmin(admin.ModelAdmin):
    list_display = ['label', 'anchor', 'order']
    list_editable = ['order']

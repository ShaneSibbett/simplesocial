from django.contrib import admin

from . import models


class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

class GroupMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'group')
    # search_fields = ['user', 'group']


admin.site.register(models.Group)
admin.site.register(models.GroupMember, GroupMemberAdmin)
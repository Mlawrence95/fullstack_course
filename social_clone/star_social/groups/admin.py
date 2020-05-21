from django.contrib import admin
from groups.models import GroupMember, Group

class GroupMemberInline(admin.TabularInline):
    model = GroupMember

admin.site.register(Group)
admin.site.register(GroupMember)

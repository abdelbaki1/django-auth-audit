# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (
    AuthLogEntry,
)


class activityAdmin(admin.ModelAdmin):

    # def has_add_permission(self, request):
    #     return False

    def has_change_permission(self, request, obj=None):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False
admin.site.register(AuthLogEntry, activityAdmin)

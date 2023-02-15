from django.contrib import admin
from .models import Session, Weekend, Task


class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', )


class TaskAdminTable(admin.TabularInline):
    model = Task
    list_display = ('title', 'weekend', 'user', 'is_send',)
    extra = 1


class WeekendAdmin(admin.ModelAdmin):
    list_display = ('title', 'session', 'is_open',)
    inlines = [
        TaskAdminTable,
    ]


admin.site.register(Session, SessionAdmin)
admin.site.register(Weekend, WeekendAdmin)

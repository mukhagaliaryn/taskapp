from django.contrib import admin
from .models import Project, Task, Solution


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'date_created', )


class SolutionAdminTable(admin.TabularInline):
    model = Solution
    list_display = ('title', 'task', 'user', 'is_send', 'date_created', )
    extra = 1


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'date_created', )
    inlines = [
        SolutionAdminTable,
    ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)

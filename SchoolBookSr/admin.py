from django.contrib import admin

from SchoolBookSr.models import Schedule, Student, New, Support


class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'updated_at', 'created_at', ]
    list_filter = ['created_at', ]


admin.site.register(New, NewsAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'grade', 'phone', 'updated_at', 'created_at', ]
    list_filter = ['grade', ]


admin.site.register(Student, StudentAdmin)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['grade', 'day_of']
    list_filter = ['grade', 'day_of']


admin.site.register(Schedule, ScheduleAdmin)


class SupportAdmin(admin.ModelAdmin):
    list_display = ['title', 'grade']
    list_filter = ['created_at', ]


admin.site.register(Support, SupportAdmin)

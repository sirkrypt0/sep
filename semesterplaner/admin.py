from django.contrib import admin

from .models import *

# Register your models here.


class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'type', 'hall', 'weekday', 'time')

    def get_name(self, obj):
        return obj.lecture.title
    get_name.admin_order_field = 'lecture'
    get_name.short_description = 'Lecture Title'


class TimeSlotInline(admin.StackedInline):
    model = TimeSlot
    extra = 0


class LectureAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Lecture',     {'fields': ['title', 'lp', 'semester', 'lecturer']}),
    ]
    inlines = [TimeSlotInline]
    list_display = ('title', 'lp', 'semester')


admin.site.register(Lecture, LectureAdmin)
admin.site.register(Lecturer)
admin.site.register(TimeSlot, TimeSlotAdmin)

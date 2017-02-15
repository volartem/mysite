from django.contrib import admin
from .models import Note, Comment, Something


class SomethingAdmin(admin.ModelAdmin):
    readonly_fields = ('format_date', )
    list_display = ('path', 'format_date', 'method', 'status_code', 'ip')

    def format_date(self, obj):
        return obj.date.strftime('%H:%M:%S %d-%m-%Y')

    format_date.short_description = 'Visited time'

admin.site.register(Note)
admin.site.register(Comment)
admin.site.register(Something, SomethingAdmin)

admin.site.site_header = "My Blog Notes"

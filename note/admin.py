from django.contrib import admin
from .models import Note, Comment, Something


class SomethingAdmin(admin.ModelAdmin):
    readonly_fields = ('date', )

admin.site.register(Note)
admin.site.register(Comment)
admin.site.register(Something, SomethingAdmin)

admin.site.site_header = "My Blog Notes"

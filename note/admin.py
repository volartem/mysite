from django.contrib import admin
from .models import Note, Comment, Something


admin.site.register(Note)
admin.site.register(Comment)
admin.site.register(Something)

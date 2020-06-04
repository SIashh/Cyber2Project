from django.contrib import admin

from .models import BlueNote, BlueWeight, RedNote, RedWeight, Tool

admin.site.register(Tool)
admin.site.register(BlueNote)
admin.site.register(BlueWeight)
admin.site.register(RedNote)
admin.site.register(RedWeight)

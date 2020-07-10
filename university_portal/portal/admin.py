from django.contrib import admin
from .models import Contact,Marks
# Register your models here.
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()
admin.site.site_header = 'University Portal'
admin.site.site_title = 'University Portal'
class ContactAdmin(admin.ModelAdmin):
	exclude = ('title',)

admin.site.register(Contact,ContactAdmin)
admin.site.register(Marks)
# admin.site.register((Contact,Marks))

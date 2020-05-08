from django.contrib import admin

# Register your models here.

from .models import Configfile

class ConfigFileAdmin(admin.ModelAdmin):
	list_display = ('name', 'config', 'model_name', 'server_ip', 'create_time', 'update_time')
	fields =  ('name', 'config', 'model_name', 'server_ip', 'remark')


admin.site.register(Configfile, ConfigFileAdmin)

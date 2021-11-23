from django.contrib import admin

from .models import Company, Profile, Application

# Register your models here.

admin.site.site_header = "Onestop Admin"
admin.site.site_title = "Onestop Admin Portal"
admin.site.index_title = "Welcome to Onestop Admin Portal"

admin.site.site_url = None
admin.site.register(Profile)
admin.site.register(Company)
admin.site.register(Application)



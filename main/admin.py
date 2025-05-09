from django.contrib import admin
from . models import About_Us

# Register your models here.

class AboutUS(admin.ModelAdmin):
    list_display = (

    )
admin.site.register(About_Us)
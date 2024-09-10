from django.contrib import admin
from .models import table, reviews, Tags
# Register your models here.

admin.site.register(table)
admin.site.register(reviews)
admin.site.register(Tags)
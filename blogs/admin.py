from django.contrib import admin
from blogs import models
# Register your models here.
admin.site.register(models.BlogPage)
admin.site.register(models.Comment)
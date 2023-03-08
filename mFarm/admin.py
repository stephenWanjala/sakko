from django.contrib import admin

from . import models

admin.site.register(models.Sacco)
admin.site.register(models.Farmer)
admin.site.register(models.Milk)
admin.site.register(models.MilkStatus)
admin.site.register(models.MilkEvaluation)
admin.site.register(models.Billing)
admin.site.register(models.MilkCollection)



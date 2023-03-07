from django.contrib import admin

from .models import Sacco

admin.site.register(Sacco)

from .models import Farmer

admin.site.register(Farmer)

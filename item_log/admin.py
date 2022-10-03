from django.contrib import admin

# Register your models here.
from .models import Item, Buyer, SalesHistory, InspectionLog

admin.site.register(Item)
admin.site.register(Buyer)
admin.site.register(SalesHistory)
admin.site.register(InspectionLog)

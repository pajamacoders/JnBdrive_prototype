from django.contrib import admin

# Register your models here.
from .models import Break, Motor, ModelType, Reducer, SafetyDevice
from .models import ProductionCompany, Product, Parts, PartsType, FaultHistory, CheckCompany, CheckHistory, SelfDiagnosis, Contract 

admin.site.register(ModelType)
admin.site.register(ProductionCompany)
admin.site.register(Product)
admin.site.register(PartsType)
admin.site.register(Parts)
admin.site.register(Reducer)
admin.site.register(Motor)
admin.site.register(Break)
admin.site.register(SafetyDevice)
admin.site.register(SelfDiagnosis)
admin.site.register(FaultHistory)
admin.site.register(CheckCompany)
admin.site.register(CheckHistory)
admin.site.register(Contract)



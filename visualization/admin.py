from django.contrib import admin
from . models import AnnualData
from . models import DepartmentData
from . models import CategaryData
from . models import companyData
from . models import GenderData
from . models import PlacedData

# Register your models here.
admin.site.register(AnnualData)
admin.site.register(DepartmentData)
admin.site.register(CategaryData)
admin.site.register(companyData)
admin.site.register(GenderData)
admin.site.register(PlacedData)


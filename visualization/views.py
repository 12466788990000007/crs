from django.shortcuts import render, redirect
from .models import AnnualData
from .models import DepartmentData
from .models import CategaryData
from .models import companyData
from .models import GenderData
from .models import PlacedData

# Create your views here.


def index(request):
    data1 = AnnualData.objects.all()
    context = {
        'data1': data1,
        
    }
    return render(request, 'visualization/index.html', context)

def index(request):
    data2 = DepartmentData.objects.all()
    context = {
        'data2': data2,
        
    }
    return render(request, 'visualization/index.html', context)

def index(request):
    data3 = CategaryData.objects.all()
    context = {
        'data3': data3,
        
    }
    return render(request, 'visualization/index.html', context)

def index(request):
    data4 = companyData.objects.all()
    context = {
        'data4': data4,
        
    }
    return render(request, 'visualization/index.html', context)

def index(request):
    data5 = GenderData.objects.all()
    context = {
        'data5': data5,
        
    }
    return render(request, 'visualization/index.html', context)

def index(request):
    data6 = PlacedData.objects.all()
    context = {
        'data6': data6,
        
    }
    return render(request, 'visualization/index.html', context)

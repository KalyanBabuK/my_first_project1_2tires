from django.shortcuts import render

# Create your views here.
def gangavathi(request):
    return render(request,'gangavathi.html')


def tourist(request):
    return render(request,'tourist.html')


def temples(request):
    return render(request,'temples.html')


def foods(request):
    return render(request,'foods.html')
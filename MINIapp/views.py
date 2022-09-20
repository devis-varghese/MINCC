from django.shortcuts import render
from .models import courses, popular_courses


# Create your views here.
def demo(request):
    obj=courses.objects.all()
    return render(request,"index.html",{'result':obj})

def demo(request):
    obj=popular_courses.objects.all()
    return render(request,"index.html",{'result':obj})
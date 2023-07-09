from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import student


# Create your views here.
def index(request):
    Students = student.objects.all()
    context = {
        'Students':Students,
    }
    return render(request, 'index.html', context)

def insert(request):
    if request.method == 'POST':
        std_name = request.POST.get('std_name')
        dept = request.POST.get('dept')
        section = request.POST.get('section')
        subject = request.POST.get('subject')

        std_obj = student.objects.create(
            name=std_name,
            department=dept,
            section=section,
            subject=subject,
        )      
        std_obj.save()
        messages.success(request, 'Sutdent insert successfully')
        return redirect('/')
    return render(request, 'form.html')
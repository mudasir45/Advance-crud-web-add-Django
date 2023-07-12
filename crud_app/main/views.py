from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import student


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

def deleteStd(request, id):
    try:   
        std_obj = student.objects.get(id = id)
        std_obj.delete()
    except Exception as e:
        print(e)

    messages.info(request, 'Student Deleted Sucessfully!')
    return redirect('/')


def updateStd(request, id):
    obj = student.objects.filter(id=id).first()
    Students = student.objects.all()
    if request.method == 'POST':
        std_name = request.POST.get('std_name')
        dept = request.POST.get('dept')
        section = request.POST.get('section')
        subject = request.POST.get('subject')
        
        std_obj = student.objects.get(id = id)
        std_obj.name = std_name
        std_obj.department = dept
        std_obj.section = section
        std_obj.subject = subject
        std_obj.save()
        messages.info(request, 'Student updated Sucessfully!')
        return redirect('/')
    label = True
    context = {
        'obj':obj,
        'label':label,
        'Students':Students,
    }
    return render(request, 'index.html', context)
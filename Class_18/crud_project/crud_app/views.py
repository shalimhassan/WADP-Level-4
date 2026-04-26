from django.shortcuts import render
from crud_app.models import TeacherModel

# Create your views here.
def home_page(request):
  return render(request, 'home.html')

def teacher_page(request):
  teacher_data =TeacherModel.objects.all()
  context={
    
    'teacher_data': teacher_data
  }
  return render(request, 'teacher_list.html',context=context)

def teacher_delete(request,'teacher_list.html',context)

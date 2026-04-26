from django.urls import path
from crud_app.views import*


urlpatterns = [
  path('',home_page,name='home_page'),
  path('teacher/',teacher_page,name='teacher_list'),
]
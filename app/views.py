from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *

# Create your views here.

#This is function based view for returning string

def fbv_string(request):
    return HttpResponse('<h1> This is function based view string </h1>')


#CBV for returning string

class cbv_string(View):
        def get(self,request):
            return HttpResponse('<h1> This is class based view function </h1>')
        
#FBV for returning Html Page

def fbv_html(request):
     return render(request,'fbv_html.html')


class CBV_html(View):
     def get(self,request):
          return render(request,'CBV_html.html')


def fbv_form(request):
     TFO=TopicForm()
     d={'TFO':TFO}

     if request.method=='POST':
          TFOD=TopicForm(request.POST)
          if TFOD.is_valid():
               TFOD.save()
               return HttpResponse('data is inserted successfully')
     return render(request,'fbv_form.html',d)

class CBV_form(View):
     def get(self,request):
          TFO=TopicForm()
          d={'TFO':TFO}
          return render(request,'CBV_form.html',d)
     
def post(self,request):
     TFD=TopicForm(request.POST)
     if TFD.is_valid():
          TFD.save()
          return HttpResponse('data is inserted successfully')
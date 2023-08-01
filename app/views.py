from django.shortcuts import render
from django.views.generic import View,TemplateView
from app.forms import *
from django.http import HttpResponse
# Create your views here.


class Data_Render(View):
    def get(self,request):
        d={'name':'KING NVN'}
        return render(request,'Data_Render.html',d)

class CBV_Insert_Student(View):
    def get(self,request):
        SFO=StudentMF()
        d={'SFO':SFO}
        return render(request,'Insert_Student.html',d)

    def post(self,request):
        SFD=StudentMF(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Data inserted succefully .....!')


class Display_html_page(TemplateView):
    template_name='Display_html_page.html'
from django.shortcuts import render

from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import FormView

from myapp.models import Deparetment,Docter,Booking
from myapp.forms import bookingForm

class DocterView(View):
    def get(self,request,*args,**kwargs):
        dic_docs={
            'doctors':Docter.objects.all()
        }
        return render(request,'docter.html',dic_docs)
    
class DepartmentView(View):
    def get(self,request,*args,**kwargs):
        dic_dept={
            'dept':Deparetment.objects.all()
        }
        return render(request,'department.html',dic_dept)  

class AboutView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'about.html')

class BookingView(View):
        model=Booking
        form_class=bookingForm
        template_name='booking.html'

        def get(self,request,*args,**kwargs):
            form=self.form_class
            return render(request,self.template_name,{"form":form})
        def post(self,request,*args,**kwargs):
            form=self.form_class(request.POST)
            if form.is_valid:
                form.save()
                return render(request,'confirmation.html')
            return render(request,self.template_name,{"form":form})




class HomeView(View):
      def get(self,request,*args,**kwargs):
        return render(request,'home.html')  

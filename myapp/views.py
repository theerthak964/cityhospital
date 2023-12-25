from django.shortcuts import render

from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView,TemplateView

from myapp.models import Deparetment,Docter,Booking
from myapp.forms import bookingForm

class DocterView(ListView):
    model=Docter
    template_name="docter.html"
    context_object_name="doctors"

    
class DepartmentView(ListView):
    model=Deparetment
    template_name="department.html"
    context_object_name="dept"
  

class AboutView(TemplateView):
     template_name="about.html"
   

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




class HomeView(TemplateView):
     template_name="home.html"
  

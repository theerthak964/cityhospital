from django import forms
from myapp.models import Booking

class bookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields="__all__"
        widgets={
            "p_name":forms.TextInput(attrs={"class":"form-control"}),
            "p_phone":forms.TextInput(attrs={"class":"form-control"}),
            "p_email":forms.EmailInput(attrs={"class":"form-control"}),
            "dep_name":forms.TextInput(attrs={"class":"form-control"}),
            "doc_name":forms.Select(attrs={"class":"form-control"}),
            "booking_date": forms.DateInput(attrs={"class": "form-control", "id": "datepicker"}),


        }

        labels = {
           'p_name':'Patient Name',
           'p_phone':'Phone Number',
           'p_email':'Email',
           'dep_name':'Department Name',
           'doc_name':'Doctor Name',
           'booking_date':'Booking Date',
        }
   

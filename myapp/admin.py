from django.contrib import admin
from myapp.models import Deparetment,Docter,Booking


admin.site.register(Deparetment)
admin.site.register(Docter)

class Bookingadmin(admin.ModelAdmin):
    list_display=('id','p_name','p_email','p_phone','doc_name','booking_date','bookedon')

admin.site.register(Booking,Bookingadmin)    
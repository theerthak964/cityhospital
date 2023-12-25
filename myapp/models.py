from django.db import models



class Deparetment(models.Model):
    dep_name=models.CharField(max_length=200)
    dep_discription=models.TextField()
    

    def __str__(self):
        return self.dep_name
    
    
class Docter(models.Model):
    doc_name=models.CharField(max_length=200)
    doc_spec=models.CharField(max_length=200)
    dep_name=models.ForeignKey(Deparetment,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to="docters",blank=True) 

    def __str__(self) :
        return 'Dr.' + self.doc_name + ' - (' + self.doc_spec + ')'

class Booking(models.Model):
    p_name=models.CharField(max_length=200)
    p_email=models.EmailField()
    p_phone=models.CharField(max_length=10)
    doc_name=models.ForeignKey(Docter,on_delete=models.CASCADE)
    booking_date=models.DateField()
    bookedon=models.DateField(auto_now=True)   

    def __str__(self) -> str:
        return self.p_name






   

    

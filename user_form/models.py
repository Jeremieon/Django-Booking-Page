from django.db import models
import random
import string
# Create your models here.
N=10
def rand_num():
    return ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))

class Booking(models.Model):
    name = models.CharField(max_length=200)
    booking_date = models.DateField()
    description=models.TextField(blank=True)
    Booking_ref=models.CharField(max_length=10,default=rand_num,unique=True)

    def __str__(self):
        return self.Booking_ref
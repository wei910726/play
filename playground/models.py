from django.db import models
# Create your models here.


class Cust(models.Model):
    cust_name = models.CharField(max_length=16)
    cust_code = models.CharField(max_length=16)
    address = models.CharField(max_length=32)
    create_date = models.DateField(auto_now=True)
    cust_state = models.CharField(max_length=3)

    def __str__(self):
        return self.cust_name


class Credit(models.Model):
    cust_id = models.IntegerField()
    create_date = models.DateField(auto_now=True)
    modify_date = models.DateField(auto_now=True)
    credit_value = models.IntegerField()
















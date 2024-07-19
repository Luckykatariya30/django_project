from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=121 , null=False)
    location = models.CharField(max_length=121)

    def __str__(self):
        return self.name
    

class Role(models.Model):
    name = models.CharField(max_length=121 , null=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    fname = models.CharField(max_length=232 , null=False)
    lname = models.CharField(max_length=232)
    dept = models.ForeignKey(Department , on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    role = models.ForeignKey(Role , on_delete=models.CASCADE)
    phone = models.IntegerField(default=1234567890)
    hire_date = models.DateField()

    def __str__(self):
        return "%s  %s  %s" %(self.fname , self.lname , self.role)

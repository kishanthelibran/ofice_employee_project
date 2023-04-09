from django.db import models

# Create your models here.


class Department(models.Model):
    dept = models.CharField(max_length=30, null=False)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.dept


class Role(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonous = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s %s %s %s %s %s" % (self.first_name, self.last_name, self.dept, self.salary, self.bonous, self.role, self.phone, self.hire_date)

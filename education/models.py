from django.db import models

class Courses(models.Model):
    name=models.CharField(max_length=150)
    price=models.PositiveIntegerField()
    duration=models.DateField()

    def __str__(self):
        return self.name

class Teachers(models.Model):
    full_name=models.CharField(max_length=150)
    status=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    course=models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

class Students(models.Model):
    full_name=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=14)
    parents_phone_number=models.CharField(max_length=14)
    telegram_link=models.CharField(max_length=40)
    address=models.CharField(max_length=50)
    course=models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teachers, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
    

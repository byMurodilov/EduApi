from django.db import models


class Courses(models.Model):
    name = models.CharField(max_length=50, unique=True)
    subject = models.CharField(max_length=11, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Corrected attribute
    davomiyligi = models.IntegerField()

    def __str__(self) -> str:
        return self.name





class Teachers(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=45)
    status = models.CharField(max_length=50)
    tajriba = models.TextField()

    def __str__(self) -> str:
        return self.full_name





class Students(models.Model):
    full_name = models.CharField(max_length=33, unique=True)
    phone_num = models.DecimalField(max_digits=13, decimal_places=0, unique=True)  
    parents_phone_num = models.DecimalField(max_digits=13, decimal_places=0, unique=True)  
    telegram_link = models.CharField(max_length=41, unique=True)
    address = models.CharField(max_length=100)
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teachers, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.full_name
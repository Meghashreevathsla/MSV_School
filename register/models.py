from django.db import models

# Create your models here.
class allStudet(models.Model):
    stu_id = models.IntegerField()
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    pw = models.CharField(max_length=4)
     

    def __str__(self):
        return str(self.name)
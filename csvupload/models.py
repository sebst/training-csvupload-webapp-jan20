from django.db import models

# Create your models here.
class Period(models.Model):
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

class Upload(models.Model):
    file_name = models.CharField(max_length=64)
    csv_file = models.FileField(upload_to='uploads/%Y/%m/%d/',null=True)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    def __str__(self):
        return self.file_name
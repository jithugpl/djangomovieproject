from django.db import models

# Create your models here.
class Filmapp(models.Model):
    cover=models.FileField(upload_to='film/cover',null=True,blank=True)
    name=models.CharField(max_length=20)
    year=models.IntegerField()
    details=models.CharField(max_length=20)

    def _str_(self):
        return self.name

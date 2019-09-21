from django.db import models
    

class CIE10Code(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=250)
    source = models.CharField(max_length=50)
    level = models.IntegerField()
    depends_on = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    multiple_descriptions = models.TextField()

    def __str__(self):
        return f'{self.code}: {self.description}'
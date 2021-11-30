from django.db import models

# Create your models here.


class Visitor(models.Model):
    name = models.CharField(max_length=200)
    visit_date = models.DateTimeField(auto_now_add=True)
    fp = models.SlugField(max_length=32)
    components = models.JSONField(null=True)
 
    def __str__(self):
        return self.name
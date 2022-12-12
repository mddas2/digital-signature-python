from django.db import models
from django.conf import settings

class Files(models.Model):
    user = models.ForeignKey(, related_name="childs",on_delete=models.CASCADE,null=True)

# Create your models here.

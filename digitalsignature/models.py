from django.db import models
from django.conf import settings

class Files(models.Model):
    user_id = models.IntegerField()
    unsigned_file =  models.FileField(upload_to='user/documents', null=True)
    signed_file =  models.FileField(upload_to='user/documents', null=True)

# Create your models here.

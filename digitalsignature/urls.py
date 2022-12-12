from django.urls import path
from . import UploadPdf

urlpatterns = [
    #**********User Authentication******************************************
    path('upload-pdf', UploadPdf.UploadPdf, name='UploadPdf'),
    path('pdf-lists', UploadPdf.UploadPdf, name='UploadPdf'),
    path('sign-pdf', UploadPdf.UploadPdf, name='UploadPdf'),

]
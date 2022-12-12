from django.urls import path
from . import UploadPdf

urlpatterns = [
    #**********User Authentication******************************************
    path('upload-pdf', UploadPdf.UploadPdf, name='UploadPdf'),
    path('pdf-lists', UploadPdf.PdfList, name='PdfList'),
    path('sign-pdf', UploadPdf.UploadPdf, name='UploadPdf'),

]
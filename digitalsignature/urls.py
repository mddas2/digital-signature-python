from django.urls import path
from . import UploadPdf,sign_pdf

urlpatterns = [
    #**********User Authentication******************************************
    path('upload-pdf', UploadPdf.UploadPdf, name='UploadPdf'),
    path('', UploadPdf.PdfList, name='PdfList'),
    path('sign-pdf/<int:id>', sign_pdf.sign_file, name='SignPdf'),

]
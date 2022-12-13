from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from digitalsignature.models import Files

# https://www.pdftron.com/documentation/python/guides/features/signature/certify-pdf/
# Create your views here.
def PdfList(request):
    files = Files.objects.all()

    data = {
        'files' : files,
    }
    return render(request,'page_type/partials/list.html',data) #return render(request,'report/application-lists.html',data)

def UploadPdf(request):
    if request.POST:
        if 'unsigned_file' in request.FILES:
            unsigned_file = request.FILES['unsigned_file']
        else:
            messages.error(request,'file can not be null')
            return redirect(PdfList)

    fileobj = Files()
    fileobj.unsigned_file = unsigned_file
    fileobj.user_id = 1
    fileobj.save()
    return redirect(PdfList)


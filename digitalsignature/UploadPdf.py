from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def PdfList(request):
    data = {
        'name' : 'manoj',
        'class' : 'six',
    }
    return render(request,'page_type/partials/list.html',data) #return render(request,'report/application-lists.html',data)

def UploadPdf(request):
    if request.POST:
        
        return HttpResponse("this is upload pdf")

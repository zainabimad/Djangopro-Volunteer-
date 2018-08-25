from django.shortcuts import render
from .form import Fileform
from django.shortcuts import redirect
from .models import Uploaded
def files(request):
    if request.method=='POST':
        form=Fileform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form=Fileform()
    return render(request,'upload.html',{'form':form})

def studio(request):
    loa=Uploaded.objects.all( )
    return render(request,'studio.html',{'loa':loa})

# Create your views here.
def details(request,id):
   det=Uploaded.objects.filter(id=id)
   return render(request,'Details.html',{'det':det})

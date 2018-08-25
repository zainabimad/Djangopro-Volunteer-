from django.shortcuts import render
from django.http import HttpResponse
from .models import Volunteers,Authentication
from .form import Vols
from django.contrib.auth import logout,authenticate
from django.shortcuts import redirect
# Create your views here.user
def index(request):
    if request.method== 'POST':
        logout(request)
    return render(request,'Index.html')
def about(request):
    return render(request,'about.html')
def vol_add(request):
  auths= Authentication.objects.filter(user=request.user)
  for i in auths:
      if i.user_type=='manger':


         if request.method == 'POST':
          form = Vols(request.POST)
          if form.is_valid():
             form.save()
             msg='تمت الاضافة بنجاح'
          return render(request,'vol_add.html',{'form':form,'msg':msg})
         else:
          form=Vols

         return render(request,'vol_add.html',{'form':form})
      else:
          return HttpResponse('لا توجد صلاحية')
def vol_list(request):
    if request.user.is_authenticated:
        vol=Volunteers.objects.all()
        search_trem = ''
        if 'search' in request.GET:
            search_trem=request.GET['search']
            vol=vol.filter(name__contains=search_trem)
        if 'ordera' in request.GET:
            vol=vol.order_by('name')
        if 'orderd' in request.GET:
            vol = vol.order_by('-name')
        return render(request ,'vol_list.html',{'voln':vol})
    else:
       return redirect('login')

def stddetails(request,id):
    lis=Volunteers.objects.filter(id=id)
    return render(request,'stddetails.html',{'lis':lis})
def edit(request,id):
    msg=''
    lic=Volunteers.objects.filter(id=id)
    if request.method == 'POST':
      form = Vols(request.POST,instance=lic.get(id=id))
      if form.is_valid():
         form.save()
         msg='تم التعديل'
         return render(request,'edit.html',{'form':form,'edit_mode':True,'lis':lic,'msg':msg})
    else:
        form=Vols(instance=lic.get(id=id))
    return render(request,'edit.html',{'form':form,'edit_mode':True,'lis':lic,'msg':msg})
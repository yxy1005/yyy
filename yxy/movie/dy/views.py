from django.shortcuts import render
from django.http import HttpResponse
from moive_s import savedata
from.models import DyModels
def index(request,page=0):
    page=int(page)
    if page>1:
        return render(request,'index.html',context={'model_list':DyModels.objects.all()[(page-1)*25:page*25],'up':page+1})
    else:
        return render(request,'index.html',context={'model_list':DyModels.objects.all()[:25]})
def pa(request):
    savedata()
    return HttpResponse('ok')
def movie(request,id):
    model=DyModels.objects.get(id=id)
    return render(request,'content.html',context={'title':model.title,'content':model.content,'link':model.link})

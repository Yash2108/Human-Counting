from django.shortcuts import render,redirect
from .forms import Trainlog
from .models import Train
from .util_func import main
import os

def train_list(request):
    obj = Train.objects.all()
    context = { "obj": obj}
    return render(request,"traincrud/train_list.html",context)


def train_log(request, id=0):
    if request.method == "GET":
        if id == 0:
            log = Trainlog()
        else:
            train = Train.objects.get(pk=id)
            log = Trainlog(instance=train)
        return render(request,"traincrud/train_log.html", {'log':log})
    else:
        if id==0:    
            log = Trainlog(request.POST, request.FILES)
        else:
            train = Train.objects.get(pk=id)
            log=Trainlog(request.POST, request.FILES,  instance = train,)
        
        # print(log.data['OutputImage'])
        
        if log.is_valid():
            obj = log.save()
            print(obj.TrainImage.url)
            print(obj.OutputImage)
            # print(os.getcwd())
            obj.OutputImage = main(os.getcwd()+obj.TrainImage.url)
            obj.save()
            return redirect('/list')

def train_delete(request, id=0):
    train = Train.objects.get(pk=id)
    train.delete()
    return redirect('/list')
from django.shortcuts import render,redirect
from .forms import Trainlog,Video_form
from .models import Train,Video
from .util_func import main
import os
from .pointrend import count_in_image

def train_list(request):
    obj = Train.objects.all()
    all_videos = Video.objects.all()
    context = {
        "obj": obj,
        "all": all_videos
     }
    return render(request,"traincrud/train_list.html",context)

def train_video(request):
    all_videos = Video.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/list')
    else:
        form=Video_form()
    return render(request,'traincrud/train_video.html',{"form":form,'all':all_videos})

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
            obj.OutputImage = count_in_image(os.getcwd()+obj.TrainImage.url)
            obj.save()
            return redirect('/list')


def train_delete(request, id=0):
    train = Train.objects.get(pk=id)
    train.delete()
    return redirect('/list')
def video_delete(request, id=0):
    x=Video.objects.get(pk=id)
    x.delete()
    return redirect('/list')
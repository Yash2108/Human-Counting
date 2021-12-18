from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Trainlog,Video_form,CreateUserForm
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
    return render(request,"humancounter/train_list.html",context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('web')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('web')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'humancounter/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('train_insert')
    
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('web')
	else:
		formreg = CreateUserForm()
		if request.method == 'POST':
			formreg = CreateUserForm(request.POST)
			if formreg.is_valid():
				formreg.save()
				user = formreg.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('web')
			
        
		context = {'formreg':formreg}
		return render(request, "humancounter/register.html", context)


def train_video(request):
    all_videos = Video.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            obj1=form.save()
            obj1.OutputVideo = main(os.getcwd()+obj1.video.url)
            obj1.save()
            return redirect('/list')
    else:
        form=Video_form()
    return render(request,'humancounter/train_video.html',{"form":form,'all':all_videos})

def train_log(request, id=0):
    if request.method == "GET":
        if id == 0:
            log = Trainlog()
        else:
            train = Train.objects.get(pk=id)
            log = Trainlog(instance=train)
        return render(request,"humancounter/train_log.html", {'log':log})
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

@login_required(login_url='login')
def train_web(request):
    return render(request, "humancounter/train_web.html")
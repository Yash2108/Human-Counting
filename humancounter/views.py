from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Trainlog,Video_form,CreateUserForm
from .models import Train,Video
# from .util_func import main
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
import threading
import cv2
from .yolo import image_feed, video_feed, live_feed
import os
# from .pointrend import count_in_image

def train_list(request):
    obj = Train.objects.all()
    all_videos = Video.objects.all()
    context = {
        "obj": obj,
        "all": all_videos,
        "logged_in":request.user.is_authenticated
     }
    return render(request,"humancounter/train_list.html",context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('web', {"logged_in":request.user.is_authenticated})
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

		context = {"logged_in":request.user.is_authenticated}
		return render(request, 'humancounter/login.html', context)

def logoutUser(request):
	logout(request)
	return render(request, 'humancounter/train_log.html', {"logged_in":request.user.is_authenticated})
    
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('web', {"logged_in":request.user.is_authenticated})
	else:
		formreg = CreateUserForm()
		if request.method == 'POST':
			formreg = CreateUserForm(request.POST)
			if formreg.is_valid():
				formreg.save()
				user = formreg.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('web', {"logged_in":request.user.is_authenticated})
			
        
		context = {'formreg':formreg, "logged_in":request.user.is_authenticated}
		return render(request, "humancounter/register.html", context)


def train_video(request):
    all_videos = Video.objects.all()
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            obj1=form.save()
            obj1.OutputVideo = video_feed(os.getcwd()+obj1.video.url)
            obj1.save()
            return redirect('/list', {"logged_in":request.user.is_authenticated})
        else:
            print("Invalid")
    else:
        form=Video_form()
    return render(request,'humancounter/train_video.html',{"form":form,'all':all_videos, "logged_in":request.user.is_authenticated})

def train_log(request, id=0):
    if request.method == "GET":
        if id == 0:
            log = Trainlog()
        else:
            train = Train.objects.get(pk=id)
            log = Trainlog(instance=train)
        return render(request,"humancounter/train_log.html", {'log':log, "logged_in":request.user.is_authenticated})
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
            obj.OutputImage = image_feed(os.getcwd()+obj.TrainImage.url)
            obj.save()
            return redirect('/list', {"logged_in":request.user.is_authenticated})


def train_delete(request, id=0):
    train = Train.objects.get(pk=id)
    train.delete()
    return redirect('/list', {"logged_in":request.user.is_authenticated})
def video_delete(request, id=0):
    x=Video.objects.get(pk=id)
    x.delete()
    return redirect('/list', {"logged_in":request.user.is_authenticated})

# @login_required(login_url='login')
# def train_web(request):
#     return render(request, "humancounter/train_web.html"

# def gen():
#     live_feed()

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        # _, jpeg = cv2.imencode('.jpg', image)
        # return jpeg.tobytes()
        return image

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        print(type(frame))
        frame = live_feed(frame)
        _, jpeg = cv2.imencode('.jpg', frame)
        print(type(frame))
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
@login_required(login_url='login')
@gzip.gzip_page
def train_web_cam(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass
       
       
@login_required(login_url='login')
def train_web(request):
    return render(request,"humancounter/train_web.html", {"logged_in":request.user.is_authenticated})

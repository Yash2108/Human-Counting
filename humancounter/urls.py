from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/',views.train_list, name='train_list'),
    path('<int:id>', views.train_log, name = 'train_update'),
    path('delete/<int:id>', views.train_delete, name = 'train_delete'),
    path('delete-videos/<int:id>',views.video_delete,name='video_delete'),
    path('', views.train_log,name='train_insert'),
    path('video/', views.train_video, name='train_video'),
    path('web/',views.train_web, name="web"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

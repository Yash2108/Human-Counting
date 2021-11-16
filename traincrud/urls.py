from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/',views.train_list, name='train_list'),
    path('<int:id>', views.train_log, name = 'train_update'),
    path('delete/<int:id>', views.train_delete, name = 'train_delete'),
    path('', views.train_log,name='train_insert')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

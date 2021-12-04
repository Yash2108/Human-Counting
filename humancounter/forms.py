from django import forms
from .models import Train,Video


class Trainlog(forms.ModelForm):

    class Meta:
        model = Train
        fields = '__all__'
            

        

    def __init__(self,*args,**kwargs):
        super(Trainlog,self).__init__(*args,**kwargs)

class Video_form(forms.ModelForm):
    class Meta:
        model=Video
        fields='__all__'

    def __init__(self,*args,**kwargs):
        super(Video_form,self).__init__(*args,**kwargs)


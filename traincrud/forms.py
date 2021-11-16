from django import forms
from .models import Train


class Trainlog(forms.ModelForm):

    class Meta:
        model = Train
        fields = '__all__'
            

        

    def __init__(self,*args,**kwargs):
        super(Trainlog,self).__init__(*args,**kwargs)
        



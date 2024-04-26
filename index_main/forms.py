from .models import Articles
from django.forms import ModelForm,TextInput, DateTimeInput,Textarea, SelectDateWidget
#from django import forms
class ArticlesForm(ModelForm):
 class Meta:
  model=Articles
  fields=['title','anons', 'full_text','date']
  widgets={
  'title':TextInput(attrs={'class': 'form-control', 'placeholder': 'Məqalənin adı'}),
  'anons':TextInput(attrs={'class': 'form-control', 'placeholder': 'Xülasə'}),
  'full_text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Mətn'}),
  # 'date':SelectDateWidget(attrs={'class': 'form-control'}),
  'date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Tarix'}),
  }



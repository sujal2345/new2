from django import forms
from .models import Post,Type,SubType

choices=Type.objects.all().values_list('name','name')
choices2=SubType.objects.all().values_list('subty','subty')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')
        widgets = {
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'usernames':forms.TextInput(attrs={'class':'form-control', 'value':'','id':'elder','type':'hidden'}),
            'facilities':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'type':forms.Select(choices=choices,attrs={'class':'form-control'}),
            'subtype':forms.Select(choices=choices2,attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),   
        }
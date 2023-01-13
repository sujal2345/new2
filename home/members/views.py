from django.views import generic    
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class UserregistrationForm(generic.CreateView):
    form=UserCreationForm
    template_name='register.html'
    success_url=reverse_lazy('login')
from django.urls import path
from .views import UserregistrationForm
urlpatterns = [
    path ('register/',UserregistrationForm.as_view(),name='register')
    ]
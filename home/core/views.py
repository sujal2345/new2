from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView, UpdateView,DeleteView
from .models import Post,Type
from .forms import PostForm
from django.urls import reverse_lazy
def index(request):
    return render(request, 'index.html')

class Homeview(ListView):
    model=Post
    template_name="index.html"
    def get_context_data(self, *args, **kwargs):
        Type_menu=Type.objects.all()
        context = super(Homeview,self).get_context_data(*args, **kwargs)
        context["Type_menu"]=Type_menu
        return context
def CategoryView(request,type_name):
    type_view=Post.objects.filter(type=type_name)
    return render(request, 'category.html',{'type_name':type_name, 'type_view':type_view})

def SubcategoryView(request,subty_name):
    subty_view=Post.objects.filter(subtype=subty_name)
    return render(request, 'subcategory.html',{'subty_name':subty_name, 'subty_view':subty_view})
    
def search_results(request):
    if request.method == 'POST':
        searched=request.POST['searched']
        find=Post.objects.filter(address__contains=searched)
        return render(request,'searchresult.html',{'searched':searched,'find':find})
class PostDetailview(DetailView):
    model=Post
    template_name='detailview.html'
class PostDeleteView(DeleteView):
    model=Post
    template_name='delete.html'
    success_url=reverse_lazy('index')
class PostCreateView(CreateView):
    model=Post
    form_class=PostForm
    template_name='addpost.html'
class PostUpdateView(UpdateView):
    model=Post
    template_name='editpost.html' 
    fields=['address','facilities','main_image','secondary_image','third_image','type','subtype']

def Buy(request):
    return render(request, 'category.html')
def Rent(request):
    return render(request, 'subcategory.html')
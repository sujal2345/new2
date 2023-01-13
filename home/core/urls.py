from django.urls import path
from core import views
from .views import PostCreateView,PostDeleteView,PostUpdateView,PostDetailview,Homeview
urlpatterns = [
    path('',Homeview.as_view(),name="index"),
    path('article/<int:pk>',PostDetailview.as_view(),name='article'),
    path('add_post/',PostCreateView.as_view(),name='addpost'),
    path('article/edit/<int:pk>',PostUpdateView.as_view(),name='edit'),
    path('article/<int:pk>/remove',PostDeleteView.as_view(),name='delete'),
    path('type/<str:type_name>', views.CategoryView,name='category'),
    path('type/Fitness', views.Buy,name='Buy'),
    path('type/Other', views.Rent,name='Rent'),
    path('subcategory/<str:subty_name>', views.SubcategoryView,name='subcategory'),
    path('search_results', views.search_results,name='search-results')

]
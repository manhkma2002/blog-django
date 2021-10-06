from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>', views.post, name='post-detail'),
    path('blog/', views.blog, name='post-list'),
    path('search/', views.search, name='search')
]

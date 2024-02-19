"""web_app_python_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostCreateView.as_view(), name='post_create_post'),
    path('<int:pk>/', views.PostRetriveView.as_view(), name='get_retrive_post'),
    path('update/<int:pk>/', views.PostUpdateView.as_view(), name='put_update_post'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='delete_post'),
    path('list/', views.PostListView.as_view(), name='get_list_post'),
]

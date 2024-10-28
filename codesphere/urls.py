"""
URL configuration for codesphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.SignUpView.as_view(),name="signup"),
    path('signin/',views.SignInView.as_view(),name="signin"),
    path('index/',views.IndexView.as_view(),name="index"),
    path('signout/',views.LogoutView.as_view(),name="signout"),
    path('change/',views.UserProfileEditView.as_view(),name="profile-edit"),
    path('project/add/',views.ProjectCreateView.as_view(),name="project-add"),
    path('myworks/all',views.MyProjectListView.as_view(),name="my-works"),
    path('project/<int:pk>/change/',views.ProjectUpdateView.as_view(),name="project-update"),
    path('project/<int:pk>/details/',views.ProjectDetailView.as_view(),name="project-details"),
    
   

    

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
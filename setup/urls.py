"""
URL configuration for setup project.

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
from network.views import CreatePostView,GetPostsView,UpdatePostView,DeletePostView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("create",CreatePostView.as_view(),name="create_post_view"),
    path("posts",GetPostsView.as_view(),name="get_posts_view"),
    path("update/<int:post_id>",UpdatePostView.as_view(),name="update_post_view"),
    path("delete/<int:post_id>",DeletePostView.as_view(),name="delete_post_view"),
]

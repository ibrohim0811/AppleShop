"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app.views import (
    ProductView, ProductDetailView, UserInfoDetailView, 
    UserRegisterView, EnteranceTemplateView, UserLoginView,
    ProfileSettings, SupportView, CartTemplateView, CommentUserCreateView,
    user_out
    )

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", EnteranceTemplateView.as_view(), name='enterance'),
    path("product/<int:pk>", ProductDetailView.as_view(), name='product'),
    path("register/", UserRegisterView.as_view(), name='register'),
    path("login/", UserLoginView.as_view(), name='login'),
    path("profile/<int:id>", UserInfoDetailView.as_view(), name='info'),
    path("logout/", user_out, name='logout'),
    path("main/", ProductView.as_view(), name='main_page'),
    path("profile_settings/", ProfileSettings.as_view(), name='profile_settings'),
    path("support/", SupportView.as_view(), name='support'),
    path("mycart/", CartTemplateView.as_view(), name='cart'),
    path("comment_create/", CommentUserCreateView.as_view(), name='comment')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
handler403 = "app.views.custom_403"
handler404 = "app.views.custom_404"

from django.shortcuts import render, redirect
from .models import Products
from django.utils import timezone
from datetime import timedelta
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import login, logout

from .models import Users
from .forms import UserRegisterForm, UserLoginForm
from .mixin import NotLoginRequiredMixin

class ProductListView(ListView):
    queryset = Products.objects.all()
    context_object_name = 'products'
    template_name = 'index.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        now = timezone.now()
        
        for p in queryset:
            
            p.is_new = (now - p.created_at <= timedelta(days=1))
        
        return queryset   
 
    
class ProductDetailView(DetailView):
    model = Products
    template_name = 'detail.html'
    context_object_name = 'product' 


class UserRegisterView(NotLoginRequiredMixin, CreateView):
    model = Users
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = '/'
    
class UserLoginView(NotLoginRequiredMixin, FormView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = '/'
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = Users.objects.filter(username=username).first()
        if user and user.check_password(password):
            login(self.request, user)
            return redirect('/')
        return super().form_valid(form)

class EnteranceTemplateView(TemplateView):
    template_name = 'enterance.html'


class UserInfoDetailView(LoginRequiredMixin, DetailView):
    model = Users
    template_name = 'user_info.html'
    context_object_name = 'user'
    pk_url_kwarg = 'id'


def user_out(request):
    logout(request)  
    return redirect('/')
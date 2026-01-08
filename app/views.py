import requests
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Products
from django.utils import timezone
from datetime import timedelta
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import login, logout

from .models import Users, Comment
from .forms import UserRegisterForm, UserLoginForm, CommentCreateForm
from .mixin import NotLoginRequiredMixin

class ProductView(ListView):
    queryset = Products.objects.all()
    context_object_name = 'products'
    template_name = 'index.html'
    @property
    def is_new(self):
        return timezone.now() - self.created_at <= timedelta(days=1)
    
    
    
    def get_queryset(self):
        
        data = super().get_queryset()
        search = self.request.GET.get('search')
        if search is None:
            products = Products.objects.all()
            return products 
        else:
            data = Products.objects.filter(name__icontains=search)
            return data
    

from django.shortcuts import render

def custom_403(request, exception):
    return render(request, "errors/403.html", status=403)
    
def custom_404(request, exception):
    return render(request, "errors/404.html", status=404)
    
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

class ProfileSettings(LoginRequiredMixin, View):
    template_name = 'profile_settings.html'
    
    def get(self, request):
        profile = request.user  
        return render(request, self.template_name, {'profile': profile})
    
    def post(self, request):
        profile = request.user  
        image = request.FILES.get('profile_image')
        if image:
            profile.image = image
            profile.save()
        return redirect('/')


class SupportView(View):
    template_name = 'support.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        username = request.POST.get("username")
        about = request.POST.get("about")
        from dotenv import load_dotenv
        import os
        load_dotenv()
        BOT_TOKEN = os.getenv('BOT_TOKEN')
        CHAT_ID = os.getenv('CHAT_ID')

        text = f"👤 {username}\n📝 {about}"

        
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    
        requests.post(url=url, data=data)

        return redirect("/")

class CartTemplateView(TemplateView):
    template_name = 'cart.html'

def user_out(request):
    logout(request)  
    return redirect('/')

class CommentUserCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentCreateForm
    success_url = '/'
    template_name = 'detail.html'
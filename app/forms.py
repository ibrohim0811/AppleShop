from django.forms import ModelForm, Form
from django.forms import CharField, PasswordInput
from django.contrib.auth.hashers import make_password
from .models import Users, Comment


class UserRegisterForm(ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'password']
        
    def clean_password(self):
        password = self.cleaned_data.get('password')
        return make_password(password)
    
class UserLoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput)
    

class SearchForm(Form):
    search = CharField(max_length=100, required=False)
    

class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'username', 'product']
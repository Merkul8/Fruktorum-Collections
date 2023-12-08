from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Collection, Bookmark


class UserRegisterForm(UserCreationForm):
    """ Форма для регистрации пользователей """
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail',  widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class UserLoginForm(AuthenticationForm):
    """ Форма для авторизации пользователей """
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))    
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CollectionForm(forms.ModelForm):
    """ Форма добавления и изменения коллекции """
    class Meta:
        model = Collection
        fields = ["title", "description"]


class BookmarkForm(forms.ModelForm):
    """ Форма для создания закладки, так же 
    для добавления новой закладки в коллекцию """
    class Meta:
        model = Bookmark
        fields = ['url']


class BookmarkAddToCollectionForm(forms.Form):
    """ Форма для добавления закладки из созданых """
    bookmark = forms.ModelChoiceField(queryset=Bookmark.objects.none())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(BookmarkAddToCollectionForm, self).__init__(*args, **kwargs)
        self.fields['bookmark'].queryset = Bookmark.objects.filter(user=user)


from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)  
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))

class ProfileForm(forms.Form):
    profile_pic = forms.ImageField()

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre_completo', 'email', 'telefono', 'nacionalidad', 'provincia', 'codigo_postal', 'ciudad', 'direccion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_completo'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-control'})
        self.fields['nacionalidad'].widget.attrs.update({'class': 'form-control'})
        self.fields['provincia'].widget.attrs.update({'class': 'form-control'})
        self.fields['codigo_postal'].widget.attrs.update({'class': 'form-control'})
        self.fields['ciudad'].widget.attrs.update({'class': 'form-control'})
        self.fields['direccion'].widget.attrs.update({'class': 'form-control'})
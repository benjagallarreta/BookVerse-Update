from django.contrib import messages
from django.urls import reverse_lazy

from django.shortcuts import redirect, render

from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout

from .models import Usuario
from Usuario.forms import LoginForm, RegistroForm



class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'user.html'  # Nombre del template que vas a crear
    context_object_name = 'usuario'

    def get_object(self):
        return self.request.user  # Obtiene el usuario actual


class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'edit_user.html'
    fields = [
        'nombre_completo',
        'email',
        'telefono',
        'nacionalidad',
        'provincia',
        'codigo_postal',
        'ciudad',
        'direccion',
    ]
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Tu perfil ha sido actualizado correctamente.")
        response = super().form_valid(form)
        return response

    def get_object(self):
        return self.request.user  # Obtiene el usuario actual
    
class RegistroView(View):
    def get(self, request):
        form = RegistroForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("Usuario autenticado, redirigiendo al home...")
                return redirect('home')
            else:
                print("Autenticación fallida.")
            
        return render(request, 'register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Usuario autenticado, redirigiendo al home...")
                return redirect('home')
            else:
                form.add_error(None, "Nombre de usuario o contraseña incorrectos")
                
        return render(request, 'login.html', {'form': form})

class CustomLogoutView(View):
    def post(self, request):
        logout(request)  # Cierra la sesión del usuario
        return redirect('home')
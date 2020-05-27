from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _

class PasswordReset(PasswordResetView):
    template_name = 'accounts/password_reset.html'

class PasswordResetDone(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

def login_(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, _('Connexion réussie !'))
            return redirect('profile')
        else:
            messages.error(request, _('Formulaire invalide.'))
    else:
        form = AuthenticationForm(request)
    return render(request, 'accounts/login.html', {
        'form': form
    })

@login_required
def logout_(request):
    logout(request)
    messages.success(request, _('Vous êtes maintenant déconnecté.'))
    return redirect('home')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _('Utilisateur créé avec succès !'))
            return redirect('home')
        else:
            messages.error(request, _('Formulaire invalide.'))
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {
        'form': form
    })

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Mot de passe mis à jour !'))
            return redirect(password_change)
        else:
            messages.error(request, _('Formulaire invalide.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {
        'form': form
    })

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.db import models
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from account.models import Profile, Contact
from blog_app.models import Post, ResearchArticle
@login_required
def data_analysis(request):
    return render(request, 'account/pages/analysis.html', {'section': 'data_analysis'})

@login_required
def research_scientifique(request):
    articles = ResearchArticle.objects.all().order_by('-id')
    return render(request, 'account/pages/scientific.html', {
        'articles': articles, 
        'section': 'research_scientifique'
    })

@login_required
def database_repo(request):
    return render(request, 'account/pages/database.html', {'section': 'database'})

@login_required
def support(request):
    return render(request, 'account/pages/support.html', {'section': 'support'})

@login_required
def tools(request):
    return render(request, 'account/pages/tools.html', {'section': 'tools'})

@login_required
def community(request):
    return render(request, 'account/pages/community.html', {'section': 'community'})

@login_required
def contact_view(request): # أو contact حسب ما هو مسمى في urls.py
    return render(request, 'account/pages/contact.html', {'section': 'contact'})

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST) # type: ignore
        if form.is_valid():
            form.save()
            messages.success(request, "📨 Message envoyé avec succès !") # type: ignore
            return redirect('contact')
    else:
        form = ContactForm() # type: ignore

    return render(request, 'account/pages/contact.html', {
        'form': form,
        'section': 'contact'
    })

# --- دوال الحساب والتسجيل ---

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form}) 

def mutation_analysis(request):
    return render(request, "account/pages/mutation_analysis.html")


def bioinformatics_analysis(request):
    return render(request, "account/pages/bioinformatics_analysis.html")


def rna_seq_analysis(request):
    return render(request, "account/pages/rna_seq_analysis.html")

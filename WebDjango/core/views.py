from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect


from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

#Creación de vistas básicas de web

def home(request):
    return render(request, "inicio.html")

def about(request):
    return render(request, "about.html")




def some_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        form2 = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            form2.instance.user = user
            form2.save()
            return redirect('name-of-some-other-view')
    else:
        form = UserCreationForm()
        form2 = ProfileForm()
    return render(request, 'name-of-some-template.html', {'form': form, 'form2': form2})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('feed')
    else:
        form = UserRegisterForm()
    context = { 'form' : form }
    return render(request, 'register.html', context)

@login_required
def post(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Post enviado')
			return redirect('feed')
	else:
		form = PostForm()
	return render(request, 'post.html', {'form' : form })



def profile(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
		posts = user.posts.all()
	else:
		posts = current_user.posts.all()
		user = current_user
	return render(request, 'profile.html', {'user':user, 'posts':posts})

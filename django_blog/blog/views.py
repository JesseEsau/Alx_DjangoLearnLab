from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserChangeForm
from .models import Post

from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import AuthorRequiredMixin

from django.urls import reverse


class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = "blog/register.html"
    template_name_suffix = 'form'
    success_url = '/profile'


class Login(LoginView):
    template_name = 'blog/login.html'


@login_required
def ProfileView(request):
    user = request.user

    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            redirect('profile')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, "blog/profile.html", {'form': form})


# class Logout(LogoutView):
#     template_name = 'blog/logout.html'

class NewPost(CreateView):
    model = Post
    template_name = "blog/new_post.html"
    fields = '__all__'
    success_url = "/posts"


class Posts(ListView):
    model = Post
    template_name = "blog/posts.html"


class PostDetail(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class PostEdit(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Post
    template_name = "blog/edit_post.html"
    fields = '__all__'
    success_url = "/posts"

    def handle_no_permission(self):
        return redirect('login')


class PostDelete(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = "/posts"

    def handle_no_permission(self):
        return redirect('login')

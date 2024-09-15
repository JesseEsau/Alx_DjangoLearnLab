from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm, CommentForm
from .models import Post
from .models import Comment
from .mixins import UserPassesTestMixin

from django.urls import reverse, reverse_lazy


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
    template_name = "blog/post_form.html"
    fields = '__all__'
    success_url = "/posts"


class Posts(ListView):
    model = Post
    template_name = "blog/posts_list.html"


def PostDetail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post=pk)
    form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, "blog/post_detail.html", context)


class PostEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog/update_post.html"
    fields = '__all__'
    success_url = "/posts"

    def handle_no_permission(self):
        return redirect('login')


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = "/posts"

    def handle_no_permission(self):
        return redirect('login')


# views for Comments
@login_required
def CommentCreateView(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post_id)
    # else:
    #     form = CommentForm()
    return render(request, "blog/comment_form.html", {"form": form, 'post': post})


class CommentListView(ListView):
    model = Comment
    template_name = "blog/comments_list.html"


# class CommentDetailView(DetailView):
#     model = Comment
#     template_name = "blog/comment_detail.html"


class CommentEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/update_comment.html"

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post_id})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "blog/delete_comment.html"

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.post_id})

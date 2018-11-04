from django.shortcuts import render, redirect
from .forms import TitleForm, PostForm, CommentForm, UpdateCommentForm
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'body', 'category', 'image']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.image = self.request.FILES
        form.save()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'body', 'category', 'image']
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Post.objects.for_user(user=self.request.user)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Post.objects.for_user(user=self.request.user)

class PostDetView(View):
    def get(self, request, pk):
        context = {
            'post': Post.objects.get(pk=pk),
            'comments': Post.objects.get(pk=pk).comments.all()
        }
        return render(request, 'posts/post_detail.html', context)


class CommentCreateView(CreateView, LoginRequiredMixin):
    model = Comment
    fields = ['message',]
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs['fk'])
        form.save()
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['message',]
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Comment.objects.for_user(user=self.request.user)

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Comment.objects.for_user(user=self.request.user)

@login_required
def add_comment(request, fk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.cleaned_data['user']
            message = form.cleaned_data['message']
            post = Post.objects.get(pk=fk)
            comment = Comment()
            comment.user = user
            comment.message = message
            comment.post = post
            comment.save()
            return redirect('index')
    else:
        form = CommentForm()
    context = {
        'form': form,
        'users': User.objects.all(),
    }
    return render(request, 'posts/add_comment.html', context)

@login_required
def delete_post(request, pk):
    post = Post.objects.get(pk= pk)
    post.delete()
    return redirect('/')

@login_required
def update_post(request, pk):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post.objects.get(pk=pk)
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    context = {
        'form': form,
        'post': Post.objects.get(pk=pk)
    }
    return render(request, 'posts/update_post.html', context)

@login_required
def delete_comment(request, fk, pk):
    comment = Comment.objects.get(pk= pk)
    comment.delete()
    return redirect('..')

@login_required
def update_comment(request, fk, pk):
    if request.method == 'POST':
        form = UpdateCommentForm(request.POST)
        if form.is_valid():
            comment = Comment.objects.get(pk=pk)
            comment.message = form.cleaned_data['message']
            comment.save()
            return redirect('..')
    else:
        form = UpdateCommentForm()
    context = {
        'form': form,
        'comment': Comment.objects.get(pk=pk)
    }
    return render(request, 'posts/update_comment.html', context)
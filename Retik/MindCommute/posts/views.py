# Utility Functions
from django.shortcuts import render
from django import forms
from django.shortcuts import reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
# Model Imports
from .models import Post, Comment

# Generic Class Views
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

class PostList(LoginRequiredMixin, ListView):
    model = Post
    ordering = ['-created','-modified']

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['headline', 'description']
    success_url = '/forum'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentForm(forms.Form):
    comment = forms.CharField()

class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    ordering = ['-id']
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['comment_form'] = CommentForm()
        return context
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = comment.objects.get(id = reply_id)
            comment = Comment(
            author = request.user,
            post = self.get_object(),
            text = comment_form.cleaned_data['comment'],
            reply = None,
            )
            comment.save()
        else:
            raise Exception
        return redirect(reverse('postdetail', args=[self.get_object().id]))

from django.shortcuts import render, get_object_or_404 # импорт отображения 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import (ListView, # импорты работы со статьями
 DetailView, 
 CreateView, 
 UpdateView,
 DeleteView)
from .models import Post 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # импорт для работы к доступам 


def home(request):
    data = {
        'news': Post.objects.all(),

    }
    return render(request, 'blog/home.html', data)

class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    model = Post
    success_url = 'blog/home.html'

    def test_func(self):
        news = self.get_object() # берем объект и сохраняем
        if self.request.user == news.avtor: 
            return True
        else:
            return False

class ShowNewView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name  = 'news'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        ctx = super(ShowNewView, self).get_context_data(**kwargs) # берем все значения 
        ctx['title'] = 'main page of blog'
        return ctx

class UserAllNewsView(ListView):
    model = Post
    template_name = 'blog/user_news.html'
    context_object_name  = 'news'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(avtor = user).order_by('-date')

    def get_context_data(self, **kwargs):
        ctx = super(UserAllNewsView, self).get_context_data(**kwargs) # берем все значения 
        ctx['title'] = f"All posts { self.kwargs.get('username')}"
        return ctx        

class NewsDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        ctx = super(NewsDetailView, self).get_context_data(**kwargs)
        ctx['title'] = Post.objects.filter(pk=self.kwargs['pk']).first()
        return ctx

    
    

class CreateNewsView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Post
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        else:
            return False





def contacti(request):
    return render(request, 'blog/contacti.html')
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from blog.forms import ArticleForm
from blog.models import Article, Category


def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'articles': articles})
def index(request):
    return redirect('blog:home')
def profile(request):
    articles = Article.objects.filter(user=request.user).order_by('id')
    return render(request, 'blog/profile.html', {'articles': articles})
def football(requrest):
    category = Category.objects.get(title='Футбол')
    articles = Article.objects.filter(category=category).order_by('id')
    return render(requrest, 'blog/football.html', {'articles': articles})
def judo(request):
    category = Category.objects.get(title='Дзюдо')
    articles = Article.objects.filter(category=category).order_by('id')
    return render(request, 'blog/judo.html', {'articles': articles})
def detail_delete(request,article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'blog/detail_delete.html', {'object': article})

class ArticleDetailView(DetailView):
    queryset = Article.objects.all()
    template_name = 'blog/detail.html'

class ArticleCreateView(CreateView):
    model = Article
    # title = forms.CharField(label='Название', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Введите название статьи'}))
    # description = forms.CharField(label='Статья', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': 'Напишите статью'}))
    form_class = ArticleForm
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:home')
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)





class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/update.html'
    success_url = reverse_lazy('blog:home')

class ArticleDeleteView(DeleteView):
    model = Article
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('blog:home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
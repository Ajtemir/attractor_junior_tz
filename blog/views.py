from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from blog.forms import ArticleForm
from blog.models import Article, Category


@login_required(login_url='login')
def home(request):
    articles = Article.objects.all()
    return render(request, 'blog/home.html', {'articles': articles})


def index(request):
    return redirect('blog:home')


@login_required(login_url='login')
def profile(request):
    articles = Article.objects.filter(user=request.user).order_by('id')
    return render(request, 'blog/profile.html', {'articles': articles})


@login_required(login_url='login')
def football(request):
    try:
        category = Category.objects.get(title='Футбол')
        articles = Article.objects.filter(category=category).order_by('id')
    except:
        articles = None

    return render(request, 'blog/football.html', {'articles': articles})


@login_required(login_url='login')
def judo(request):
    try:
        category = Category.objects.get(title='Дзюдо')
        articles = Article.objects.filter(category=category).order_by('id')
    except:
        articles = None
    return render(request, 'blog/judo.html', {'articles': articles})


@login_required(login_url='login')
def box(request):
    try:
        category = Category.objects.get(title='Бокс')
        articles = Article.objects.filter(category=category).order_by('id')
    except:
        articles = None
    return render(request, 'blog/box.html', {'articles': articles})


@login_required(login_url='login')
def basketball(request):
    try:
        category = Category.objects.get(title='Баскетбол')
        articles = Article.objects.filter(category=category).order_by('id')
    except:
        articles = None
    return render(request, 'blog/basketball.html', {'articles': articles})


def detail_delete(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'blog/detail_delete.html', {'object': article})


class ArticleDetailView(DetailView):
    queryset = Article.objects.all()
    template_name = 'blog/detail.html'


class ArticleCreateView(CreateView):
    model = Article
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
    success_url = reverse_lazy('blog:home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

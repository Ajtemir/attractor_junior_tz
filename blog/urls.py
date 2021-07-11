from django.urls import path

from blog import views
from blog.views import ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleCreateView

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('football/', views.football, name='football'),
    path('judo/', views.judo, name='judo'),
    path('basketball/', views.basketball, name='basketball'),
    path('box/', views.box, name='box'),
    path('detail_delete/<int:article_id>/', views.detail_delete, name='detail_delete'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
    path('add/', ArticleCreateView.as_view(), name="create"),
]
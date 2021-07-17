from django.contrib.auth import get_user_model
from django.test import TestCase

from blog.models import Article, Category

User =get_user_model()

class ArticleTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='tester', password='testing')
        self.parent_category = Category.objects.create(title='командный вид')
        self.category = Category.objects.create(title='Футбол', parent_id=Category.objects.get(title='командный вид'))
        self.article = Article.objects.create(title='Евро-2021', category=self.category, user=self.user)

    def test_first(self):
        article = Article.objects.get(id=1)
        field_label = article._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название статьи')

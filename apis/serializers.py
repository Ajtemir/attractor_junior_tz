from rest_framework import serializers

from blog.models import Category, Article


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

class ArticleSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    def get_image(self, article):
        request = self.context.get('request')
        image_url = article.image.url
        return request.build_absolute_uri(image_url)

    class Meta:
        model = Article
        fields = '__all__'
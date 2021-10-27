from rest_framework import serializers

from .models import Article, Author

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'description','body', 'created_date','published_date','author')

    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
    created_date = serializers.DateTimeField()
    published_date = serializers.DateTimeField()
    

    def create(self, validated_data):
        return Article.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description) 
        instance.body = validated_data.get('body', instance.body)
        instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.author_id = validated_data.get('author', instance.author)

        instance.save()
        return instance

class AuthorSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ("id", "name", "email","articles")

    name = serializers.CharField(max_length=120)
    email = serializers.CharField()
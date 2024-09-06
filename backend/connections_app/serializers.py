from rest_framework import serializers
from .models import ConnectionsGame, Category, Word

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['word']

class CategorySerializer(serializers.ModelSerializer):
    words = serializers.SerializerMethodField()
    is_py_code = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['category', 'words', 'is_py_code', 'difficulty', 'explanation']

    def get_words(self, obj):
        # Return list of words for the category
        return [word.word for word in obj.words.all()]

    def get_is_py_code(self, obj):
        # Check for Python code or leave empty, customize logic as needed
        return [word.word for word in obj.words.all() if obj.is_py_code]

        pass

class ConnectionsGameSerializer(serializers.ModelSerializer):
    game = CategorySerializer(many=True, source='categories')

    class Meta:
        model = ConnectionsGame
        fields = ['title', 'created_at', 'author', 'num_categories', 'words_per_category', 'game']
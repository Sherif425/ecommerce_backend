from rest_framework import serializers
from .models import Category, Product


class CatalogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]

    
class ProductSerializer(serializers.ModelSerializer):
    category = CatalogCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True)    
    
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "category",
            "category_id",
            "created_at",
            "updated_at",
        ]    
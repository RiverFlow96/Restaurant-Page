from rest_framework import serializers
from .models import Category, MenuItem, Reservation, GalleryImage, Review, ContactInfo


class CategorySerializer(serializers.ModelSerializer):
    menu_items_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'order', 'slug', 'menu_items_count', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_menu_items_count(self, obj):
        return obj.menu_items.filter(available=True).count()


class MenuItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = MenuItem
        fields = [
            'id', 'name', 'description', 'price', 'category', 'category_name',
            'image', 'available', 'order', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'id', 'name', 'email', 'phone', 'date', 'time', 'guests',
            'special_requests', 'status', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'status', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['status'] = 'pending'
        return super().create(validated_data)


class ReservationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'name', 'date', 'time', 'guests', 'status', 'created_at']


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image', 'caption', 'alt_text', 'order', 'created_at']
        read_only_fields = ['id', 'created_at']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'client_name', 'rating', 'comment', 'is_approved', 'created_at']
        read_only_fields = ['id', 'is_approved', 'created_at']

    def create(self, validated_data):
        validated_data['is_approved'] = False
        return super().create(validated_data)


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'client_name', 'rating', 'is_approved', 'created_at']


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['id', 'address', 'phone', 'email', 'opening_hours', 'map_embed', 'is_active', 'updated_at']
        read_only_fields = ['id', 'updated_at']
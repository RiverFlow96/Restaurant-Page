from rest_framework import serializers
from .models import Category, MenuItem, Reservation, GalleryImage, Review, ContactInfo


class CategorySerializer(serializers.ModelSerializer):
    menu_items_count = serializers.SerializerMethodField()
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'order', 'slug', 'menu_items_count', '_links', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_menu_items_count(self, obj):
        return obj.menu_items.filter(available=True).count()

    def get__links(self, obj):
        request = self.context.get('request')
        if request:
            from .hateoas import generate_links
            return generate_links(request, 'categories', obj.id, ['update', 'delete'])
        return None


class MenuItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    _links = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = [
            'id', 'name', 'description', 'price', 'category', 'category_name',
            'image', 'available', 'order', '_links', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get__links(self, obj):
        request = self.context.get('request')
        if request:
            from .hateoas import generate_links
            return generate_links(request, 'menu', obj.id, ['update', 'delete'])
        return None


class ReservationSerializer(serializers.ModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = [
            'id', 'name', 'email', 'phone', 'date', 'time', 'guests',
            'special_requests', 'status', '_links', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'status', 'created_at', 'updated_at']

    def get__links(self, obj):
        request = self.context.get('request')
        if request:
            from .hateoas import generate_links
            actions = ['update', 'partial_update', 'delete'] if request.user.is_staff else []
            return generate_links(request, 'reservations', obj.id, actions)
        return None


class ReservationListSerializer(serializers.ModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ['id', 'name', 'date', 'time', 'guests', 'status', '_links', 'created_at']

    def get__links(self, obj):
        request = self.context.get('request')
        if request:
            from .hateoas import generate_links
            return generate_links(request, 'reservations', obj.id)
        return None


class GalleryImageSerializer(serializers.ModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = GalleryImage
        fields = ['id', 'image', 'caption', 'alt_text', 'order', '_links', 'created_at']
        read_only_fields = ['id', 'created_at']

    def get__links(self, obj):
        request = self.context.get('request')
        if request:
            from .hateoas import generate_links
            return generate_links(request, 'gallery', obj.id, ['update', 'delete'])
        return None


class ReviewSerializer(serializers.ModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'client_name', 'rating', 'comment', 'is_approved', '_links', 'created_at']
        read_only_fields = ['id', 'is_approved', 'created_at']

    def get__links(self, obj):
        request = self.context.get('request')
        if request:
            from .hateoas import generate_links
            actions = ['update', 'delete'] if request.user.is_staff else []
            return generate_links(request, 'reviews', obj.id, actions)
        return None


class ReviewListSerializer(serializers.ModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'client_name', 'rating', 'is_approved', '_links', 'created_at']

    def get__links(self, obj):
        request = self.context.get('request')
        if request:
            from .hateoas import generate_links
            return generate_links(request, 'reviews', obj.id)
        return None


class ContactInfoSerializer(serializers.ModelSerializer):
    _links = serializers.SerializerMethodField()

    class Meta:
        model = ContactInfo
        fields = ['id', 'address', 'phone', 'email', 'opening_hours', 'map_embed', 'is_active', '_links', 'updated_at']
        read_only_fields = ['id', 'updated_at']

    def get__links(self, obj):
        request = self.context.get('request')
        if request:
            from .hateoas import generate_links
            actions = ['partial_update'] if request.user.is_staff else []
            return generate_links(request, 'contact', 1, actions)
        return None
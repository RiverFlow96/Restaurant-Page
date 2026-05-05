from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from django.db.models import Q

from .models import Category, MenuItem, Reservation, GalleryImage, Review, ContactInfo
from .serializers import (
    CategorySerializer, MenuItemSerializer,
    ReservationSerializer, ReservationListSerializer,
    GalleryImageSerializer, ReviewSerializer, ReviewListSerializer,
    ContactInfoSerializer
)
from .permissions import IsPublic
from .responses import validation_error, not_found, conflict, success, created


class StandardPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsPublic]
    pagination_class = StandardPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'order', 'created_at']
    ordering = ['order']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsPublic]
    pagination_class = StandardPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'order', 'created_at']
    ordering = ['order']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.query_params.get('category')
        available = self.request.query_params.get('available')
        price_min = self.request.query_params.get('price_min')
        price_max = self.request.query_params.get('price_max')

        if category:
            qs = qs.filter(category__slug=category)
        if available is not None:
            qs = qs.filter(available=available.lower() == 'true')
        if price_min:
            qs = qs.filter(price__gte=price_min)
        if price_max:
            qs = qs.filter(price__lte=price_max)
        return qs


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    permission_classes = [IsPublic]
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['date', 'time', 'created_at']
    ordering = ['-created_at']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_serializer_class(self):
        if self.action == 'list':
            return ReservationListSerializer
        return ReservationSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAdminUser()]
        return [IsPublic()]

    def get_queryset(self):
        qs = super().get_queryset()
        status_filter = self.request.query_params.get('status')
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        guests = self.request.query_params.get('guests')
        guests_min = self.request.query_params.get('guests_min')
        guests_max = self.request.query_params.get('guests_max')

        if status_filter:
            qs = qs.filter(status=status_filter)
        if date_from:
            qs = qs.filter(date__gte=date_from)
        if date_to:
            qs = qs.filter(date__lte=date_to)
        if guests:
            qs = qs.filter(guests=guests)
        if guests_min:
            qs = qs.filter(guests__gte=guests_min)
        if guests_max:
            qs = qs.filter(guests__lte=guests_max)
        return qs

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return validation_error(serializer.errors)
        self.perform_create(serializer)
        return created('Reserva creada correctamente. Te contactaremos para confirmar.', serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return success('Reserva eliminada correctamente')


class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = [IsPublic]
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['order', 'created_at']
    ordering = ['order']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [IsPublic]
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['rating', 'created_at']
    ordering = ['-created_at']
    throttle_classes = [AnonRateThrottle]

    def get_serializer_class(self):
        if self.action == 'list':
            return ReviewListSerializer
        return ReviewSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        rating = self.request.query_params.get('rating')
        rating_min = self.request.query_params.get('rating_min')
        rating_max = self.request.query_params.get('rating_max')

        if not self.request.user.is_staff:
            qs = qs.filter(is_approved=True)
        if rating:
            qs = qs.filter(rating=rating)
        if rating_min:
            qs = qs.filter(rating__gte=rating_min)
        if rating_max:
            qs = qs.filter(rating__lte=rating_max)
        return qs

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            if self.request.user.is_staff:
                return [IsAdminUser()]
            return [AllowAny()]
        return [IsPublic()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return validation_error(serializer.errors)
        self.perform_create(serializer)
        return created('Gracias por tu reseña. Será visible tras ser aprobada.')


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [IsPublic]
    http_method_names = ['get', 'post', 'put', 'patch']
    pagination_class = None

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    def get_object(self):
        return ContactInfo.objects.first()

    def list(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj:
            return not_found('Información de contacto')
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj:
            return not_found('Información de contacto')
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        existing = ContactInfo.objects.first()
        if existing:
            return conflict('Ya existe información de contacto. Usa PUT para actualizar.')
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return validation_error(serializer.errors)
        self.perform_create(serializer)
        return created('Información de contacto creada.', serializer.data)

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj:
            return not_found('Información de contacto')
        serializer = self.get_serializer(obj, data=request.data, partial=kwargs.get('partial', False))
        if not serializer.is_valid():
            return validation_error(serializer.errors)
        self.perform_update(serializer)
        return success('Información de contacto actualizada.', serializer.data)

    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, partial=True, **kwargs)
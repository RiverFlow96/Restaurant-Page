"""
Vistas de la API Restaurant con documentación de filtros.

Filtros disponibles por endpoint:
- /menu/: category, available, search
- /categories/: search
- /reservations/: status, date_from, date_to
- /reviews/: rating
"""

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Q

from .models import Category, MenuItem, Reservation, GalleryImage, Review, ContactInfo
from .serializers import (
    CategorySerializer, MenuItemSerializer,
    ReservationSerializer, ReservationListSerializer,
    GalleryImageSerializer, ReviewSerializer, ReviewListSerializer,
    ContactInfoSerializer
)
from .permissions import IsPublic, IsPublicOrAdmin
from .responses import error_response, validation_error, not_found, conflict, success, created


class StandardPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class CategoryViewSet(viewsets.ModelViewSet):
    """
    Endpoint: /categories/

    Filtros disponibles:
    - search: Buscar por nombre o descripción
    - page: Número de página
    - page_size: Items por página

    Ejemplos:
    - GET /api/v1/restaurant/categories/
    - GET /api/v1/restaurant/categories/?search=entrantes
    - GET /api/v1/restaurant/categories/?page=2&page_size=10
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsPublic]
    pagination_class = StandardPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.query_params.get('search')
        if search:
            qs = qs.filter(Q(name__icontains=search) | Q(description__icontains=search))
        return qs


class MenuItemViewSet(viewsets.ModelViewSet):
    """
    Endpoint: /menu/

    Filtros disponibles:
    - category: Filtrar por categoría (slug)
    - available: Filtrar por disponibilidad (true/false)
    - search: Buscar por nombre o descripción
    - page: Número de página
    - page_size: Items por página

    Ejemplos:
    - GET /api/v1/restaurant/menu/
    - GET /api/v1/restaurant/menu/?category=entrantes
    - GET /api/v1/restaurant/menu/?available=true
    - GET /api/v1/restaurant/menu/?search=risotto
    - GET /api/v1/restaurant/menu/?category=platos&available=true
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsPublic]
    pagination_class = StandardPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.query_params.get('category')
        available = self.request.query_params.get('available')
        search = self.request.query_params.get('search')

        if category:
            qs = qs.filter(category__slug=category)
        if available is not None:
            qs = qs.filter(available=available.lower() == 'true')
        if search:
            qs = qs.filter(Q(name__icontains=search) | Q(description__icontains=search))
        return qs


class ReservationViewSet(viewsets.ModelViewSet):
    """
    Endpoint: /reservations/

    Crear reserva (público):
    POST /api/v1/restaurant/reservations/
    {
        "name": "Nombre",
        "email": "email@ejemplo.com",
        "phone": "+34600000000",
        "date": "2026-06-01",
        "time": "20:00",
        "guests": 2,
        "special_requests": "Opcional"
    }

    Filtros (admin):
    - status: pending, confirmed, cancelled, completed
    - date_from: Fecha mínima
    - date_to: Fecha máxima
    """
    queryset = Reservation.objects.all()
    permission_classes = [IsPublic]
    pagination_class = StandardPagination

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

        if status_filter:
            qs = qs.filter(status=status_filter)
        if date_from:
            qs = qs.filter(date__gte=date_from)
        if date_to:
            qs = qs.filter(date__lte=date_to)
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
    """
    Endpoint: /gallery/

    Filtros disponibles:
    - page: Número de página
    - page_size: Items por página

    Ejemplo:
    - GET /api/v1/restaurant/gallery/?page=2&page_size=10
    """
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = [IsPublic]
    pagination_class = StandardPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]


class ReviewViewSet(viewsets.ModelViewSet):
    """
    Endpoint: /reviews/

    Crear reseña (público):
    POST /api/v1/restaurant/reviews/
    {
        "client_name": "Nombre",
        "rating": 5,
        "comment": "Comentario"
    }

    Filtros disponibles:
    - rating: Filtrar por puntuación (1-5)

    Ejemplos:
    - GET /api/v1/restaurant/reviews/
    - GET /api/v1/restaurant/reviews/?rating=5
    """
    queryset = Review.objects.all()
    permission_classes = [IsPublic]
    pagination_class = StandardPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return ReviewListSerializer
        return ReviewSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        rating = self.request.query_params.get('rating')

        if not self.request.user.is_staff:
            qs = qs.filter(is_approved=True)
        if rating:
            qs = qs.filter(rating=rating)
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
    """
    Endpoint: /contact/

    GET: Ver información de contacto (público)
    POST: Crear info de contacto (admin)
    PUT/PATCH: Actualizar info de contacto (admin)

    Solo permite un registro de contacto.
    """
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
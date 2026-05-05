from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from django.shortcuts import get_object_or_404

from .models import Category, MenuItem, Reservation, GalleryImage, Review, ContactInfo
from .serializers import (
    CategorySerializer, MenuItemSerializer,
    ReservationSerializer, ReservationListSerializer,
    GalleryImageSerializer, ReviewSerializer, ReviewListSerializer,
    ContactInfoSerializer
)
from .permissions import IsPublic, IsPublicOrAdmin


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsPublic]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsPublic]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.query_params.get('category')
        available = self.request.query_params.get('available')

        if category:
            qs = qs.filter(category__slug=category)
        if available is not None:
            qs = qs.filter(available=available.lower() == 'true')
        return qs


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    permission_classes = [IsPublic]

    def get_serializer_class(self):
        if self.action == 'list':
            return ReservationListSerializer
        return ReservationSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAdminUser()]
        return [IsPublic()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"success": True, "message": "Reserva creada correctamente. Te contactaremos para confirmar."},
            status=status.HTTP_201_CREATED
        )


class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    permission_classes = [IsPublic]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    permission_classes = [IsPublic]

    def get_serializer_class(self):
        if self.action == 'list':
            return ReviewListSerializer
        return ReviewSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Review.objects.all()
        return Review.objects.filter(is_approved=True)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            if self.request.user.is_staff:
                return [IsAdminUser()]
            return [AllowAny()]
        return [IsPublic()]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"success": True, "message": "Gracias por tu reseña. Será visible tras ser aprobada."},
            status=status.HTTP_201_CREATED
        )


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
    permission_classes = [IsPublic]
    http_method_names = ['get', 'post', 'put', 'patch']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]

    def get_object(self):
        return ContactInfo.objects.first()

    def list(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj:
            return Response({"detail": "No encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj:
            return Response({"detail": "No encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        existing = ContactInfo.objects.first()
        if existing:
            return Response(
                {"detail": "Ya existe información de contacto. Usa PUT para actualizar."},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if not obj:
            return Response(
                {"detail": "No existe información de contacto. Crea una primero."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(obj, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
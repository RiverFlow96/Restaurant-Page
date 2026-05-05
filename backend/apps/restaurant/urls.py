from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, MenuItemViewSet, ReservationViewSet,
    GalleryImageViewSet, ReviewViewSet, ContactInfoViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'menu', MenuItemViewSet, basename='menu')
router.register(r'reservations', ReservationViewSet, basename='reservation')
router.register(r'gallery', GalleryImageViewSet, basename='gallery')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'contact', ContactInfoViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]
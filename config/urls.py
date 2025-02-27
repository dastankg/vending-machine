from django.contrib import admin
from django.urls import path
from apps.products.views import ProductListAPIView, PurchaseProductAPIView

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/products", ProductListAPIView.as_view(), name="products-list"),
    path('api/purchase/', PurchaseProductAPIView.as_view(), name='purchase-products'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]

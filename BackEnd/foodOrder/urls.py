from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from shop.views import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    UserRegistrationView,
    login,
    OrderListCreateAPIView,
    OrderRetrieveUpdateDestroyAPIView,
    UserCreateAPIView,
    ProductCategoryCreateAPIView,
    OrderItemAPIView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('api/productcategories/', ProductCategoryCreateAPIView.as_view(), name='product-category-create'),
    path('api/orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('api/orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-retrieve-update-destroy'),
    path('api/orders/<int:order_id>/items/', OrderItemAPIView.as_view(), name='order-item-list-create'),
    path('api/create-superuser/', UserCreateAPIView.as_view(), name='user-create'),
    path('api/login/', login, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
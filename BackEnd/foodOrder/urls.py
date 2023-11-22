from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from shop.views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, UserRegistrationView, login, OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    # path('api/register/', UserRegistrationView.as_view(), name='register_user'),
    path('api/login/', login, name='login'),
    path('api/orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('api/orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-retrieve-update-destroy'),

]

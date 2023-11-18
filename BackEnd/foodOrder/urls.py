from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from shop.views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, UserRegistrationView, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    # path('api/register/', UserRegistrationView.as_view(), name='register_user'),
    path('api/login/', login, name='login'),

]

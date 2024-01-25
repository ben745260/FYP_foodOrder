from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from shop.views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, UserRegistrationView, login, OrderListCreateAPIView, OrderRetrieveUpdateDestroyAPIView, UserCreateAPIView, ProductCategoryViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.authtoken')),
    path('api/products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('api/productcategories/', ProductCategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='productcategory-list-create'),
    path('api/productcategories/<int:pk>/', ProductCategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='productcategory-retrieve-update-destroy'),
    # path('api/register/', UserRegistrationView.as_view(), name='register_user'),
    path('api/login/', login, name='login'),
    path('api/orders/', OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('api/orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-retrieve-update-destroy'),
    path('api/create-superuser/', UserCreateAPIView.as_view(), name='user-create'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

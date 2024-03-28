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
    OrderItemAPIView,
    order_list_by_table,
    UserFeedbackCreateAPIView,
    UserFeedbackRetrieveUpdateDestroyAPIView,
    sales_analysis,
    menu_analysis,
    dashboardAPI,
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
    path('api/orders/table/<int:order_table>/', order_list_by_table),
    path('api/orders/<int:order_id>/items/', OrderItemAPIView.as_view(), name='order-item-list-create'),

    path('api/feedbacks/', UserFeedbackCreateAPIView.as_view(), name='user-feedback-create'),
    path('api/feedbacks/<int:pk>/', UserFeedbackRetrieveUpdateDestroyAPIView.as_view(), name='user-feedback-retrieve-update-destroy'),

    path('api/sales-analysis/', sales_analysis, name='sales-analysis'),
    path('api/menu-analysis/', menu_analysis, name='menu-analysis'),

    path('api/dashboard/', dashboardAPI, name='dashboardAPI'),
    
    path('api/create-superuser/', UserCreateAPIView.as_view(), name='user-create'),
    path('api/login/', login, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
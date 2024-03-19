from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Sum, F


from .models import Product, Order, OrderItem, ProductCategory, UserFeedback
from .serializers import ProductSerializer, UserSerializer, OrderSerializer, ProductCategorySerializer, OrderItemSerializer, UserFeedbackSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ================================================================

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
    
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    def perform_create(self, serializer):
        serializer.save(is_active=True, is_superuser=True, is_staff=True)
# =================================================================
        
class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@api_view(['GET', 'PUT'])
def order_list_by_table(request, order_table):
    if request.method == 'GET':
        orders = Order.objects.filter(order_table=order_table)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        orders = Order.objects.filter(order_table=order_table)
        orders.update(order_checkout=True)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
class OrderItemAPIView(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        order = get_object_or_404(Order, pk=self.kwargs['order_id'])
        return OrderItem.objects.filter(order_id=order)

    def create(self, request, *args, **kwargs):
        order = get_object_or_404(Order, order_id=self.kwargs['order_id'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(order_id=order)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
    
# ================================================================
class ProductCategoryCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

# ================================================================
class UserFeedbackCreateAPIView(generics.ListCreateAPIView):
    queryset = UserFeedback.objects.all()
    serializer_class = UserFeedbackSerializer
# ================================================================
    
@api_view(['GET'])
def sales_analysis(request):
    # Calculate total sales
    total_sales = OrderItem.objects.aggregate(total_sales=Sum('product_amount'))['total_sales']

    # Calculate most popular category
    popular_category = ProductCategory.objects.annotate(num_sales=Count('product__orderitem')).order_by('-num_sales').first()

    # Calculate sales trend
    sales_trend = Order.objects.values('order_lastUpdateDate').annotate(total_sales=Sum('order_amount')).order_by('order_lastUpdateDate')

    analysis_data = {
        'totalSales': total_sales,
        'mostPopularCategory': popular_category.name if popular_category else None,
        'salesTrend': [{'date': entry['order_lastUpdateDate'], 'sales': entry['total_sales']} for entry in sales_trend]
    }

    return Response(analysis_data)

@api_view(['GET'])
def menu_analysis(request):
    # Calculate most popular menu items
    popular_items = OrderItem.objects.values('product_id__product_name').annotate(total_quantity=Sum('quantity')).order_by('-total_quantity')[:5]

    # Calculate item profitability
    item_profitability = Product.objects.annotate(profitability=F('price') * F('orderitem__quantity')).order_by('-profitability')

    analysis_data = {
        'mostPopularItems': [entry['product_id__product_name'] for entry in popular_items],
        'itemProfitability': [{'name': item.product_name, 'profitability': item.profitability} for item in item_profitability]
    }

    return Response(analysis_data)
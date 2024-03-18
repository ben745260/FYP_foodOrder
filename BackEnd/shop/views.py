from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

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
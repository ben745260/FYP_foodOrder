from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Order, ProductCategory, OrderItem, UserFeedback


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create and return a new User instance
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.is_staff = True  # Set staff status
        user.save()
        return user


class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_order_items(self, obj):
        order_items = obj.orderitem_set.all()
        return OrderItemSerializer(order_items, many=True).data


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'is_active', 'is_staff', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            is_active=validated_data['is_active'],
            is_staff=validated_data['is_staff'],
            is_superuser=validated_data['is_superuser']
        )
        return user


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'

class UserFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeedback
        fields = '__all__'
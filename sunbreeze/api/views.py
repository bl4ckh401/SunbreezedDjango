from typing import Counter
from django.core.checks import messages
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from api.models import Order, OrderItem, i_stock
from api.serializers import InvestorySerializers
from rest_framework import generics, serializers, status,permissions
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken
from django.utils import timezone


# Create your views here.


class Inventory(generics.CreateAPIView):
        serializer_class = InvestorySerializers
        query_set = i_stock.objects.all()

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class post_product(APIView):
        serializer_class = InvestorySerializers

        def post(self, request, format=None):
                        serializer = self.serializer_class(data=request.data)
                        if serializer.is_valid():
                                title = serializer.data.get('title')
                                price = serializer.data.get('price')
                                slug = serializer.data.get('slug')
                                image = serializer.data.get('image')
                                description = serializer.data.get('description')
                                query_set = i_stock.objects.filter(title=title)
                                if query_set.exists():
                                        product= query_set[0]
                                        product.title = title
                                        product.price = price
                                        product.slug = slug
                                        product.description = description
                                        product.image = image
                                        product.save(update_fields=['title', 'price', 'slug','description', 'image'])
                                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                                else:
                                        product = i_stock(
                                                title=title,
                                                price=price,
                                                description=description,
                                                image = image,
                                                slug = slug,
                                                )
                                        product.save()
                                        return Response(serializer.data, status=status.HTTP_201_CREATED)

                        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class AllProducts(APIView):
        def get(self, request, format=None):
                item = i_stock.objects.all()
                serializer = InvestorySerializers(item, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)


class AddToCart(APIView):
        def post(self, request, *args, **kwargs):
                slug = request.data.get('slug', None)
                if slug is None:
                        return Response({'Failed':'Invalid Request'}, status=status.HTTP_400_BAD_REQUEST)
                item = get_object_or_404(i_stock, slug=slug)
                
                order_item, created = OrderItem.objects.get_or_create(
                        item=item,
                        user=request.user,
                        ordered=False
                )
                order_qs = Order.objects.filter(user=request.user, ordered=False)
                if order_qs.exists():
                        order = order_qs[0]
                        # check if the order item is in the order
                        if order.items.filter(item__slug=item.slug).exists():
                                order_item.quantity += 1
                                order_item.save()
                                return Response({'success': 'Item added to cart'},status=status.HTTP_200_OK)
                        else:
                                order.items.add(order_item)
                                return Response({'success': 'Item added to cart'},status=status.HTTP_200_OK)

                else:
                        ordered_date = timezone.now()
                        order = Order.objects.create(
                        user=request.user, ordered_date=ordered_date)
                        order.items.add(order_item)
                        return Response({'success': 'Item added to cart'},status=status.HTTP_200_OK)


class GetCSRFToken(APIView):
        def get(self, request, format=None):
                return Response({'success': 'CSRF cookie set'})
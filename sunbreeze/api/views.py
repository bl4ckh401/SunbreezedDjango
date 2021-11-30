from typing import Counter
from django.core.checks import messages
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from api.models import Customer, Order, i_stock
from api.serializers import InvestorySerializers
from rest_framework import generics, serializers, status
from rest_framework.response import Response


# Create your views here.


class Inventory(generics.CreateAPIView):
        serializer_class = InvestorySerializers
        query_set = i_stock.objects.all()



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


def cart(request):
        try:
                customer = request.user.customer
        except:
                device = request.COOKIES['device']
                customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        context = {'order':order}
        return Response(status=status.HTTP_200_OK)


class GetCSRFToken(APIView):
        def get(self, request, format=None):
                return Response({'success': 'CSRF cookie set'})
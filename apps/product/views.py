from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.product.models import Product
from apps.product.serializers import ProductSerializer, PurchaseSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer


class PurchaseProductAPIView(generics.GenericAPIView):
    serializer_class = PurchaseSerializer

    def post(self, request, *args, **kwargs):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response({
                "message": "Purchase successful",
                "product": {
                    "name": result['product'].name,
                    "price": result['product'].price,
                    "remaining_count": result['product'].count
                },
                "quantity": result['quantity'],
                "remaining_money": result['remaining_money']
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

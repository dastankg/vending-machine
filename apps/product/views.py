from rest_framework import pagination, generics
from rest_framework.response import Response

from apps.product.models import Product
from apps.product.serializer import ProductSerializer




class ProductPagination(pagination.PageNumberPagination):
    page_size = 1


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response({'products' : serializer.data})

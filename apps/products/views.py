from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.products.models import Product
from apps.products.serializers import ProductSerializer, PurchaseSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample


@extend_schema(
    summary="Получение списка продуктов",
    description="Этот эндпоинт возвращает список всех доступных продуктов.",
    responses={
        200: ProductSerializer(many=True),
    },
    examples=[
        OpenApiExample(
            "Список продуктов",
            value=[
                {
                    "id": 1,
                    "name": "Товар 1",
                    "price": "100.00",
                    "count": 10
                },
                {
                    "id": 2,
                    "name": "Товар 2",
                    "price": "200.00",
                    "count": 5
                }
            ]
        )
    ]
)
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer


@extend_schema(
    summary="Покупка продукта",
    description="Этот эндпоинт используется для покупки продукта. Вы передаете ID продукта и количество, а в ответ получаете подтверждение покупки.",
    request=PurchaseSerializer,
    responses={
        200: {
            "message": "Purchase successful",
            "products": {
                "name": "string",
                "price": "decimal",
                "remaining_count": "int"
            },
            "quantity": "int",
            "remaining_money": "decimal"
        },
        400: "Ошибка валидации данных"
    },
    examples=[
        OpenApiExample(
            "Пример запроса",
            value={
                "product_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "quantity": 2,
                "money": "200.00"
            }
        ),
        OpenApiExample(
            "Пример успешного ответа",
            value={
                "message": "Purchase successful",
                "products": {
                    "name": "Книга",
                    "price": "50.00",
                    "remaining_count": 8
                },
                "quantity": 2,
                "remaining_money": "100.00"
            }
        )
    ]
)
class PurchaseProductAPIView(generics.GenericAPIView):
    serializer_class = PurchaseSerializer

    def post(self, request, *args, **kwargs):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response({
                "message": "Purchase successful",
                "products": {
                    "name": result['products'].name,
                    "price": result['products'].price,
                    "remaining_count": result['products'].count
                },
                "quantity": result['quantity'],
                "remaining_money": result['remaining_money']
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

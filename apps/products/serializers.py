import uuid

from rest_framework import serializers
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model: Product = Product
        fields: list[str] = ['id', 'name', 'price', 'count']


class PurchaseSerializer(serializers.Serializer):
    product_id: uuid = serializers.UUIDField()
    quantity: int = serializers.IntegerField(min_value=1, default=1)
    money: int = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate(self, data):
        try:
            product = Product.objects.get(id=data['product_id'])
        except Product.DoesNotExist:
            raise serializers.ValidationError({"product_id": "Указанный продукт не существуют."})
        if product.count < data['quantity']:
            raise serializers.ValidationError({f'quantity": "Недостаточно товара на складе. Имеется {product.count}'})

        total_price: float = product.price * data['quantity']
        if data['money'] < total_price:
            raise serializers.ValidationError({
                "money": f'Недостаточно средств. Общая стоимость составляет {total_price}'
            })

        data['products'] = product
        data['total_price'] = total_price
        return data

    def create(self, validated_data):
        product = validated_data['products']
        product.count -= validated_data['quantity']
        product.save()
        return {
            'products': product,
            'quantity': validated_data['quantity'],
            'remaining_money': validated_data['money'] - validated_data['total_price']
        }

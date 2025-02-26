import uuid

from rest_framework import serializers
from apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model: Product = Product
        fields: list[str] = ['name', 'price', 'count']


class PurchaseSerializer(serializers.Serializer):
    product_id: uuid = serializers.UUIDField()
    quantity: int = serializers.IntegerField(min_value=1, default=1)
    money: int = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate(self, data):
        try:
            product = Product.objects.get(id=data['product_id'])
        except Product.DoesNotExist:
            raise serializers.ValidationError({"product_id": "The specified product does not exist."})
        if product.count < data['quantity']:
            raise serializers.ValidationError({"quantity": "Not enough items in stock."})

        total_price: float = product.price * data['quantity']
        if data['money'] < total_price:
            raise serializers.ValidationError({
                "money": "Insufficient funds. Total price is {}".format(total_price)
            })

        data['product'] = product
        data['total_price'] = total_price
        return data

    def create(self, validated_data):
        product = validated_data['product']
        product.count -= validated_data['quantity']
        product.save()
        return {
            'product': product,
            'quantity': validated_data['quantity'],
            'remaining_money': validated_data['money'] - validated_data['total_price']
        }

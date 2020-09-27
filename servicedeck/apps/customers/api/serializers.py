from rest_framework import serializers

from accounts.api.serializers import UserSingUpSerializer
from customers.models import Customer


class CustomerSignUpSerializer(serializers.ModelSerializer):
    user = UserSingUpSerializer()

    class Meta:
        model = Customer
        fields = [
            'user',
            'phone',
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_obj = UserSingUpSerializer.create(UserSingUpSerializer(), validated_data=user_data)
        customer = Customer.objects.create(
            user=user_obj,
            **validated_data
        )
        customer.save()
        return customer
from rest_framework import serializers
from shop.models import Shop, Employee, Work


class WorkShopSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Work
        fields = [

        ]


class ShopSerializer(serializers.ModelSerializer):
    employees = serializers.SerializerMethodField(read_only=True)
    works = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Shop
        fields = [
            'title',
            'city',
            'street',
            'house',
            'employees',
            'works'
        ]

    def get_employees(self, object):
        return Employee.objects.filter(shop=object)

    def get_works(self, object):
        data = {
            'works': Work.objects.filter(shop=object),
            '': ''
        }
        return Work.objects.filter(shop=object)


class ShopEngineerSerializer(serializers.ModelSerializer):
    """Shop serializer to engineer."""
    class Meta:
        model = Shop
        fields = [
            'title',
            'city',
            'street',
            'house',
            'employees',
            'works'
        ]
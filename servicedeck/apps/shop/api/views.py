from rest_framework import generics, mixins
from shop.models import Shop
from .serializers import ShopSerializer


class ShopApiView(generics.ListAPIView, mixins.CreateModelMixin):
    """"""
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
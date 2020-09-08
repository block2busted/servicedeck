import json

from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View


def update_employee_detail_view(request):
    data = {
        'count': 5,
        'banana': 2
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


class JsonMixin(object):
    """"""
    def render_to_json(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context


class JsonRetrieveView(JsonMixin, View):
    """"""
    def get(self, request, *args, **kwargs):
        """"""
        data = {
            'count': 5,
            'banana': 2
        }
        return self.render_to_json(context=data)


class SerializedDetailView(View):
    """"""
    def get(self, request, *args, **kwargs):
        """"""
        obj = Shop.objects.get(id=1)
        data = serialize('json', [obj,])
        data = obj.serialize()
        return HttpResponse(data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        obj_list = User.objects.all()
        data = serialize('json', obj_list, fields=('username', 'email'))
        return HttpResponse(data, content_type='application/json')

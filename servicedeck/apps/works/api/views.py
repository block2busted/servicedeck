from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from works.models import Work
from .serializers import WorkCreateSerializer, WorkListSerializer, WorkEmployeeSerializer


class WorkCreateAPIView(generics.CreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkCreateSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class WorkListAPIView(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkListSerializer
    permission_classes = []
    authentication_classes = []


class WorkDetailAPIView(generics.RetrieveAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkListSerializer
    permission_classes = []
    authentication_classes = []

from works.models import EmployeeWork, Employee


class WorkStartAPIView(APIView):
    """"""
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        data = request.data
        work_pk = data.get('work_pk')

        employee_pk = data.get('employee_pk')

        work_obj = Work.objects.get(pk=work_pk)

        if work_obj.status == 'In Process':
            return Response({'detail': 'This work in process yet.'}, status=403)

        employee_obj = Employee.objects.get(pk=employee_pk)

        employee_work_obj = EmployeeWork.objects.create(
            employee=employee_obj,
            work=work_obj
        )

        work_obj.update_status(value='In Process')
        work_obj.save()

        employee_work_obj.save()
        response_data = {
            'work_pk': work_pk,
            'employee_pk': employee_pk
        }
        return Response(response_data, status=201)


class WorkInProcessAPIView(generics.ListAPIView):
    queryset = EmployeeWork.objects.all()
    serializer_class = WorkEmployeeSerializer
    permission_classes = []
    authentication_classes = []

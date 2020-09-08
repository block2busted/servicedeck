from rest_framework import pagination


class EmployeePagination(pagination.PageNumberPagination):
    page_size = 5
import json

from django.db import models
from django.core.serializers import serialize
from employee.models import Employee


class Work(models.Model):
    """Work model"""
    WORK_IMPORTANT = (
        ('R', 'rush'),
        ('U', 'usual'),
        ('NR', 'not rush')
    )
    WORK_TYPE = (
        ('SE', 'shop equipment'),
        ('W', 'worldwide')
    )
    important = models.CharField(choices=WORK_IMPORTANT, max_length=2, verbose_name='important work')
    type = models.CharField(choices=WORK_TYPE, max_length=2, verbose_name='Type')
    is_active = models.BooleanField(default=True, verbose_name='Is active')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    due_date = models.DateTimeField(verbose_name='Due date')

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'


class Shop(models.Model):
    """Shop model"""
    title = models.CharField(max_length=128, blank=False, verbose_name='Shop name')
    city = models.CharField(max_length=128, verbose_name='City')
    street = models.CharField(max_length=128, verbose_name='Street')
    house = models.IntegerField(verbose_name='House')
    employees = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee')
    works = models.ForeignKey(Work, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Works')

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

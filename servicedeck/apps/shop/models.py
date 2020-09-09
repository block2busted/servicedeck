from django.db import models
from employee.models import Employee

from works.models import Work


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

    def __str__(self):
        return 'Shop {1}.'.format(self.title)
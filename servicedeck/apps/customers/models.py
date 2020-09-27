from django.db import models

from django.contrib.auth import get_user_model

from works.models import Work

User = get_user_model()


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='User')
    phone = models.CharField(max_length=15, help_text='Phone', blank=True, null=True, verbose_name='Phone')
    works = models.ForeignKey(Work, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Works')

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return 'Customer {}.'.format({self.user.username})

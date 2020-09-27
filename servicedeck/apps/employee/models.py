from django.contrib.auth.models import User
from django.db import models


class Position(models.Model):
    """"""
    STATUS = (
        ('D', 'Director'),
        ('CE', 'Chief Engineer'),
        ('LS', 'Line Specialist')
    )
    status = models.CharField(choices=STATUS, max_length=2, verbose_name='Status')
    responsibilities = models.TextField(verbose_name='Responsibilities')

    class Meta:
        verbose_name = 'Position'
        verbose_name_plural = 'Positions'

    def __str__(self):
        return 'Position {}'.format(self.status)


def upload_user_photo(instance, filename):
    return 'employee/{username}{filename}'.format(username=instance.username, filename=filename)


class Employee(models.Model):
    """"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Employee username')
    first_name = models.CharField(max_length=32, verbose_name='First name')
    middle_name = models.CharField(max_length=32, verbose_name='Middle name')
    last_name = models.CharField(max_length=32, verbose_name='Last name')
    photo = models.ImageField(upload_to='employee_images', null=True, blank=True,
                              default='default.jpg', verbose_name='Photo')
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='Employee position')
    kpi = models.FloatField(verbose_name='KPI', default=0, help_text='KPI')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    @property
    def owner(self):
        return self.user

    def __str__(self):
        return 'Employee {}'.format({self.user.username})


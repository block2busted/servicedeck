from django.db import models
from django.utils import timezone

from employee.models import Employee


class Work(models.Model):
    """Work model"""
    WORK_IMPORTANT = (
        ('Rush', 'rush'),
        ('Usual', 'usual'),
        ('Not Rush', 'not rush')
    )
    WORK_TYPE = (
        ('Shop Equipment', 'shop equipment'),
        ('Worldwide', 'worldwide')
    )
    WORK_STATUS = (
        ('Is Free', 'Is Free'),
        ('In Process', 'In Process'),
        ('Ended', 'Ended')
    )

    title = models.CharField(max_length=128, default='', verbose_name='Title')
    important = models.CharField(choices=WORK_IMPORTANT, max_length=8, verbose_name='important work')
    type = models.CharField(choices=WORK_TYPE, max_length=14, verbose_name='Type')
    description = models.TextField(verbose_name='Description', default='')
    is_active = models.BooleanField(default=True, verbose_name='Is active')
    status = models.CharField(choices=WORK_STATUS, max_length=10, default='Is Free', verbose_name='status')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    due_date = models.DateTimeField(verbose_name='Due date')

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return 'Work {}.'.format(self.description)

    def update_status(self, value):
        self.status = value


class EmployeeWork(models.Model):
    """"""
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee')
    work = models.ForeignKey(Work, on_delete=models.CASCADE, verbose_name='Work')

    class Meta:
        verbose_name = 'Employee work'
        verbose_name_plural = 'Employee works'

    def __str__(self):
        return 'Work {} by {} {} employee.'.format(self.work.title, self.employee.first_name, self.employee.last_name)

    def get_deadline_time(self):
        return self.work.due_date - timezone.now()
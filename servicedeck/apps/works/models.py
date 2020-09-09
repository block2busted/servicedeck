from django.db import models
from django.utils import timezone

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
    description = models.TextField(verbose_name='Description', default='')
    is_active = models.BooleanField(default=True, verbose_name='Is active')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    due_date = models.DateTimeField(verbose_name='Due date')

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    def __str__(self):
        return 'Work {1}.'.format(self.description)


class EmployeeWork(models.Model):
    """"""
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Employee')
    work = models.ForeignKey(Work, on_delete=models.CASCADE, verbose_name='Work')

    class Meta:
        verbose_name = 'Employee work'
        verbose_name_plural = 'Employee works'

    def __str__(self):
        return 'Work {1} by {2} {3} employee.'.format(self.work.title, self.employee.first_name, self.employee.last_name)

    def get_deadline_time(self):
        return self.work.due_date - timezone.now()
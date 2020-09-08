from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        first_name = data.get('first_name', None)
        middle_name = data.get('middle_name', None)
        last_name = data.get('last_name', None)
        kpi = data.get('kpi', None)
        if first_name is None or middle_name is None or last_name is None or kpi is None:
            raise forms.ValidationError('Some of fields is required...')
        return super(EmployeeForm, self).clean(*args, **kwargs)
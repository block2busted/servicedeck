from django import forms
from .models import Shop


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['title', 'city', 'street', 'house']

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        title = data.get('title', None)
        if title == '':
            title = None
        city = data.get('city', None)
        street = data.get('street', None)
        house = data.get('house', None)
        if title is None and city is None and street is None and house is None:
            raise forms.ValidationError('Something is required')
        return super(ShopForm, self).clean(*args, **kwargs)
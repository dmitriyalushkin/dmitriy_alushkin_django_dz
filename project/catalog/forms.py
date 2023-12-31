from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                 'бесплатно', 'обман', 'полиция', 'радар']

        for obj in words:
            if obj in cleaned_data:
                raise forms.ValidationError('Ошибка, связанная с именем продукта')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
                 'бесплатно', 'обман', 'полиция', 'радар']

        for obj in words:
            if obj in cleaned_data:
                raise forms.ValidationError('Ошибка, связанная с описанием продукта')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
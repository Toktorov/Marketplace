from attr import field
from django import forms
from apps.products.models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
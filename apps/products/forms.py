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

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)
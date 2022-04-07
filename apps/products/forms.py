from django import forms
from apps.products.models import ProductComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ('message', )
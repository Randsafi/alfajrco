from django import forms

class SEED_SEARCH(forms.Form):
    search_query = forms.CharField(
        label='',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'ابحث عن منتج...', 'class': 'form-control'})
        )
        
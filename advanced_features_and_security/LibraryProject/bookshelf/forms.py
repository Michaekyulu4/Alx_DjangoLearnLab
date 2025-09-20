from django import forms


class SearchForm(forms.Form):
query = forms.CharField(
max_length=100,
required=True,
strip=True,
widget=forms.TextInput(attrs={"placeholder": "Search books..."}),
)


def clean_query(self):
q = self.cleaned_data['query']
# Add additional validation/sanitization rules here if needed
# e.g. block control characters or suspicious patterns
return q
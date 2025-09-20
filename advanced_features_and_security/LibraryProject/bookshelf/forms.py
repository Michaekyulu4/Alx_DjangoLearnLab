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

class ExampleForm(forms.Form):
    """Simple example form demonstrating CSRF token and validation."""
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Your Name",
        widget=forms.TextInput(attrs={"placeholder": "Enter your name"})
    )
    email = forms.EmailField(
        required=True,
        label="Email Address",
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email"})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Enter your message"}),
        required=True,
        label="Message"
    )
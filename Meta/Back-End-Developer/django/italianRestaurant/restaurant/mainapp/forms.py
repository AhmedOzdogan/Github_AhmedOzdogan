from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Your Name')
    email = forms.EmailField(required=True, label='Your Email')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Your Message')
class ReservationForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Your Name')
    email = forms.EmailField(required=True, label='Your Email')
    phone = forms.CharField(max_length=15, required=True, label='Your Phone Number')
    date = forms.DateField(
        required=True,
        label='Reservation Date',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    time = forms.TimeField(
        required=True,
        label='Reservation Time',
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})
    )
    people = forms.IntegerField(
        min_value=1,
        required=True,
        label='Number of People',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

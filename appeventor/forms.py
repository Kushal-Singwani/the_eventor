from django import forms
from .models import FakePayment,Feedback
import random, string

class FakePaymentForm(forms.ModelForm):
    class Meta:
        model = FakePayment
        fields = ['name', 'email', 'amount']
      

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.transaction_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        if commit:
            instance.save()
        return instance



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
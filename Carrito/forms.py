from django import forms
from Carrito.validarTarjeta import CreditCardField, ExpiryDateField, VerificationValueField

#PARA LA VALIDACION DE LA TARJETA
class PaymentForm(forms.Form):
    name_on_card = forms.CharField(max_length=50, required=True)
    card_number = CreditCardField(required=True)
    expiry_date = ExpiryDateField(required=True)
    card_code = VerificationValueField(required=True)
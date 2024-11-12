from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100,
                           label='Имя',
                           widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}))
    email = forms.EmailField(label='Электронная почта',
                             widget=forms.TextInput(attrs={'placeholder': 'Введите ваш email'}))
    message = forms.CharField(label='Сообщение',
                              widget=forms.Textarea(attrs={'placeholder': 'Введите ваше сообщение'}))

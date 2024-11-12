from django.shortcuts import render, redirect
from .models import Course
from .forms import ContactForm


courses = [
    {
        'title': 'Курс 1',
        'description': 'Описание курса 1',
        'price': 1000
    },
    {
        'title': 'Курс 2',
        'description': 'Описание курса 2',
        'price': 2000
    },
    {
        'title': 'Курс 3',
        'description': 'Описание курса 3',
        'price': 3000
    },
    {
        'title': 'Курс 4',
        'description': 'Описание курса 4',
        'price': 4000
    }
]


def course_list(request):
    return render(request, 'course_list.html', {'courses': courses})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            return render(request, 'contact_success.html', {
                'name': name,
                'email': email,
                'message': message
            })
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

from django.urls import path
from .views import contact, course_list


urlpatterns = [
    path('', course_list, name='course_list'),
    path('contact/', contact, name='contact'),
]
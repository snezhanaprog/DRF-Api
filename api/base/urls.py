from django.urls import path
from . import views


urlpatterns = [
    path("", views.endpoints),
    path("persons/", views.persons, name='persons'),
    path("sections/", views.sections, name='sections'),
    path("persons/<str:name>/", views.person_details.as_view(), name='person'),
]
#quiz앱에대한 url
from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns=[
    path("hello/",helloAPI),
    path("<int:id>/",randomQuiz)
]
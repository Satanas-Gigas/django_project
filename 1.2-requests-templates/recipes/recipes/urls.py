from django.urls import path

from calculator.views import index_view

urlpatterns = [
    path("<str:dish>/", index_view, name="recipe")
]
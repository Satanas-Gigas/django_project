from django.urls import path

from calculator.views import index_view

urlpatterns = [
    path("<str:dish>/", index_view, name="recipe")
<<<<<<< HEAD
]
=======
]
>>>>>>> bd670410bf798fea37ad23fce6cfcbada6cf2fbc

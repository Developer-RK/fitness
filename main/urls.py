from .views import HomeView,ClientView
from django.urls import path



urlpatterns = [

    path('', HomeView.as_view(), name="home"  ),
    path('clients', ClientView.as_view(), name="clients"  ),
]
from django.urls import path
from .views import attend_view

urlpatterns = [
    path('', attend_view, name="attend_view")
]
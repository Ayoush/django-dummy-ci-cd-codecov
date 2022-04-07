from django.urls import path
from . import views

urlpatterns = [
    path('org/', views.org_index, name='org_index')
]

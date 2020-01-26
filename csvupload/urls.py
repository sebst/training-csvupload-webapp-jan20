from django.contrib import admin
from django.urls import path, include

from .views import period_detail, period_list, concat
urlpatterns = [
    path('',period_list),
    path('period/<int:pk>',period_detail),
    path("concat/<int:pk>", concat)
]
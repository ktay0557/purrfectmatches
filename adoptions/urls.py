from django.urls import path
from adoptions import views

urlpatterns = [
    path('adoptions/', views.AdoptionList.as_view()),
    path('adoptions/<int:pk>/', views.AdoptionDetail.as_view()),
]

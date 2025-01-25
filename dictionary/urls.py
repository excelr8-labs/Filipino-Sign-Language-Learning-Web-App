from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dictionary'),
    path('word/<str:word>/', views.word_detail, name='word_detail'),
]

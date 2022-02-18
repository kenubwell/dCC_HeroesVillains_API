from django.urls import path
from . import views

urlpatterns = [
    path('', views.battles_list),
    path('<int:pk>/', views.battles_detail), #the int:pk is stating that the pk value has to be an integer

]
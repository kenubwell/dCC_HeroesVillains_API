from django.urls import path
from . import views

urlpatterns = [
    path('', views.supertypes_list),
    path('<int:pk>/', views.supertypes_detail), #the int:pk is stating that the pk value has to be an integer

]
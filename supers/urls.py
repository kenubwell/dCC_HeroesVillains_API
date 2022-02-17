# (2.5 points) As a developer, I want my API to serve the “supers” app’s content on the following urls paths:
# Paths must match these exactly!  | ‘127.0.0.1:8000/api/supers/<int:pk>/’

from django.urls import path
from . import views

urlpatterns = [
    path('', views.supers_list),
    #path ('../?', views.supertypes_list),
    path('<int:pk>/', views.supers_detail), #the int:pk is stating that the pk value has to be an integer

]
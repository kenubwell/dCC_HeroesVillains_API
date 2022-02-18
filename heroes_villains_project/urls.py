"""heroes_villains_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# (2.5 points) As a developer, I want my API to serve the “supers” app’s content on the following urls paths:
# Paths must match these exactly!  | ‘127.0.0.1:8000/api/supers/' - optional params

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/supers/', include('supers.urls')),
    path('api/supers/supertypes/', include('super_types.urls')), 
]

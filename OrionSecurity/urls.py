"""OrionSecurity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from acceso_obra import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/acceso_obra/', include('acceso_obra.urls')),
    path('api/v1/guardias/', include('guardias.urls')),
    path('api/v1/libro_novedades/', include('libro_novedades.urls')),
    path('api/v1/notificaciones/', include('notificaciones.urls')),
    path('api/v1/turnos/', include('turnos.urls')),

]

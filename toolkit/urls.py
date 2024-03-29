"""dictionary URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from main import views 
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('binary_to_number_converter', views.binary_to_number_converter, name='binary_to_number_converter'),
    path('number_to_binary_converter', views.number_to_binary_converter, name='number_to_binary_converter'),
    path('password_generator', views.password_generator, name='password_generator'),
    path('hours_to_seconds', views.hours_to_seconds, name='hours_to_seconds'),
    path('hours_to_minutes', views.hours_to_minutes, name='hours_to_minutes'),
    path('txt_document_to_pdf', views.txt_document_to_pdf, name='txt_document_to_pdf'),
    path('send_feedback', views.send_feedback, name='send_feedback'),
    path('', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

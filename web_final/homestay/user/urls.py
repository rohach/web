from django.urls import path

from .views import home, experiences, impact, about


urlpatterns = [
    path('', home, name='home'),
    path('experiences', experiences, name='experiences'),
    path('impact', impact, name='impact'),
    path('about', about, name='about'),

]

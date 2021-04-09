from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import home, experiences, impact, about, SignUpView, first, AddBookingView, BookingView, RoomView, RoomUpdate, RoomDelete



urlpatterns = [
    path('home', home, name='home'),
    path('experiences', experiences, name='experiences'),
    path('impact', impact, name='impact'),
    path('about', about, name='about'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', first, name='first'),
    path('addbooking', AddBookingView.as_view(), name='AddBookingView'),
    path('booking/', BookingView, name='booking' ),
    path('room/view/<int:pk>/', RoomView.as_view(), name='roomview'),
    path('room/<int:pk>/update', RoomUpdate.as_view(), name="update"),
    path('room/<int:pk>/delete', RoomDelete.as_view(), name="delete"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


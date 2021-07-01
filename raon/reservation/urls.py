from django.urls import path
from . import views
from django.conf.urls import url
app_name = "reservations"
urlpatterns = [
    url(
        regex=r'^search/$',
        view=views.NameSearch.as_view(),
        name='name_search'
    ),
    url(
        regex=r'^reservation/$',
        view=views.Reservation.as_view(),
        name='post'
    ),
]

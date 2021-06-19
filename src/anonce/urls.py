from django.urls import  path
from .views import anonce_list_view

app_name="anonce"

urlpatterns = [
    path('',anonce_list_view,name="anonce-view")
]
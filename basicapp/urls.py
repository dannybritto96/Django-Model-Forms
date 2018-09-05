from django.conf.urls import url
from . import views

app_name = "basicapp"

urlpatterns = [
    url("^$",views.index,name='index'),
]

from django.urls import path
from . import views

urlpatterns = {
    path("", views.index),

    path("activity", views.act),
    path("activityOne",views.act1),
    path("activityTwo",views.act2)
}

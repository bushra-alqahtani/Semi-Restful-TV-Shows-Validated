from django.urls import path
from . import views

urlpatterns=[

    path("",views.index),
    path("shows",views.shows),
 
    path("show/create",views.create),
    path("show/<int:id>",views.showbyid),
    path("show/<int:id>/edit",views.edit),
    path("show/<int:id>/delete",views.delete),

  
]
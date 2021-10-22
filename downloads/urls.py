from django.urls import path
from downloads import views

urlpatterns = [
    path("businessline/", views.businessline, name="businessline"),
    path("deccanchronicle/", views.dec, name="dec"),
    path("economictimes/", views.eco, name="eco"),
    path("hindustantimes/", views.hintim, name="hintim"),
    path("finacialexpress/", views.fin, name="fin"),
    path("indianexpress/", views.indexp, name="indexp"),
    path("thehindu/", views.thehindu, name= "thehindu"),
    path("brillsexp/",views.brills, name="brills"),
    path("timesofindia/", views.toi, name="toi"),
    path("tribune/", views.tribune, name="tribune"),
]

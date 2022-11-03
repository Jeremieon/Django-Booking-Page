from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^forms/',views.my_form,name='forms')

]

from django.conf.urls import url

from . import views

urlpatterns = [
	#http://127.0.0.1:8000/gstapp/
    url(r'^$', views.index, name='index'),

    #http://127.0.0.1:8000/gstapp/businesses
    url(r'^businesses/$', views.businesses, name='businesses'),

    #http://127.0.0.1:8000/gstapp/products
    url(r'^products/$', views.products, name='products'),

    #http://127.0.0.1:8000/gstapp/b2b_txn
    url(r'^b2b_txn/$', views.b2b_txn, name='b2b_txn'),

    #http://127.0.0.1:8000/gstapp/b2c_txn
    url(r'^b2c_txn/$', views.b2c_txn, name='b2c_txn'),
]
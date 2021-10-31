from django.urls import path
from . import views
urlpatterns = [
path('', views.index , name='index'),
path('register', views.register, name='register' ),
path('customer_login',views.customer_login , name= 'customer_login'),
path('customerhome',views.customerhome , name='customerhome'),
path('endtrip',views.endtrip, name='endtrip'),
path('starttrip',views.starttrip , name='starttrip'),
path('allbookings',views.allbookings , name='allbookings'),
path('payment_page',views.payment_page , name='payment_page'),
]
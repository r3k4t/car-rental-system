from django.urls import path
from . import views
urlpatterns = [
path('', views.index , name='index'),
# path('register', views.register, name='register' ),
# path('customer_login',views.customer_login , name= 'customer_login'),
path('employeeportal',views.employeeportal , name='employeeportal'),
path('employeecustomerview',views.employeecustomerview, name='employeecustomerview'),
path('employeeaddvehicle',views.employeeaddvehicle , name='employeeaddvehicle'),
path('employeeaddlocation',views.employeeaddlocation , name='employeeaddlocation'),
path('employeeaddvehicleclass',views.employeeaddvehicleclass , name='employeeaddvehicleclass'),
path('employeesendcoupon',views.employeesendcoupon , name='employeesendcoupon'),
]
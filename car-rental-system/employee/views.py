from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
import random

import sys
sys.path.append("..")

from customer.models import *

# Create your views here.



def index(request):
    return render(request, 'index.html')




def employeesendcoupon(request):


    customers = KprcIndividual.objects.all()

    if request.method == 'POST':

        discount = request.POST['discount']
        validity = request.POST['validity']
        cust_id = request.POST['cust_id']



        coupon = KprcCoupon()
        coupon.coupon_id = random.randint(1000, 9999)
        coupon.discount = discount
        coupon.validity = validity
        coupon.cust = KprcIndividual.objects.get(cust_id = KprcCustomer.objects.get(cust_id = cust_id))
        coupon.save()

        return redirect('/employeeportal')


    return render(request, 'employeesendcoupon.html', {'customer_ids': customers})



def employeeportal(request):
    return render(request, 'employeeportal.html')

def employeecustomerview(request):

    objs = KprcCustomer.objects.all()


    return render(request, 'employeecustomerview.html', {'customer_data': objs})

def employeeaddvehicle(request):

    objs = KprcVehicleclass.objects.all()


    if request.method == 'POST':
        vin = random.randint(1000, 9999)
        license = request.POST['license']
        make = request.POST['make']
        model = request.POST['model']
        year = request.POST['year']
        vehicle_class = request.POST['vehicle_class']


        vehicle = KprcVehicle()

        vehicle.vin = vin
        vehicle.license_plate_number = license
        vehicle.make = make
        vehicle.model = model
        vehicle.year = year
        vehicle.class_field = KprcVehicleclass.objects.get(class_id = vehicle_class)
        vehicle.save()

        return redirect('/employeeportal')


    return render(request, 'employeeaddvehicle.html', {'v_class': objs})


def employeeaddlocation(request):

    objs = KprcVehicleclass.objects.all()


    if request.method == 'POST':
        locationid = random.randint(1000, 9999)
        phoneno = request.POST['phoneno']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        vehicle_class = request.POST.getlist('vehicle_class')


        location = KprcLocation()

        location.location_id = locationid
        location.phone_number = phoneno
        location.street = street
        location.city = city
        location.state = state
        location.zipcode = zipcode
        location.save()


        if vehicle_class:

            for i in range(len(vehicle_class)):
                location_class = KprcLocationclass()

                # location_class.location_id = KprcLocation.objects.get(location_id = locationid)
                # location_class.class_field = KprcVehicleclass.objects.get(class_id = vehicle_class[i])
                location_class.location_id = locationid
                location_class.class_field = KprcVehicleclass.objects.get(class_id = vehicle_class[i])
                location_class.save()


        return redirect('/employeeportal')

    return render(request, 'employeeaddlocation.html', {'v_class': objs})



def employeeaddvehicleclass(request):

    if request.method == 'POST':
        classid = request.POST['classid']
        classname = request.POST['classname']
        rental_rate = request.POST['rental_rate']
        over_mileage_fee = request.POST['over_mileage_fee']
        daily_limit = request.POST['daily_limit']

        vehicle_class = KprcVehicleclass()
        vehicle_class.class_id = classid
        vehicle_class.class_name = classname
        vehicle_class.rental_rate = rental_rate
        vehicle_class.over_mileage_fee = over_mileage_fee
        vehicle_class.daily_limit = daily_limit

        vehicle_class.save()

        return redirect('/employeeportal')


    return render(request, 'employeeaddvehicleclass.html')














from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.db.models import F
from django.contrib import messages
from .models import *
from django.utils.timezone import datetime
import random
from django.utils.timezone import make_aware

# Create your views here.



def index(request):

    return render(request, 'index.html')


def register(request):

    objs = KprcCorporation.objects.all()

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        type = request.POST['type']




        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        print('user created')

        customer = KprcCustomer()
        customer.cust_fname = firstname
        customer.cust_lname = lastname
        customer.cust_phone = phone
        customer.cust_street = street
        customer.cust_city = city
        customer.cust_state = state
        customer.cust_email = email
        customer.cust_type = type

        customer.save()




        id_kprc = KprcCustomer.objects.get(cust_fname=firstname, cust_lname=lastname, cust_email = email)
        cust_id = id_kprc.cust_id



        if type == 'kprc_individual':
            dlno = request.POST['dlno']
            insurancecompany = request.POST['insurancecompany']
            policyno = request.POST['policyno']

            individual_customer = KprcIndividual()
            individual_customer.cust_id = cust_id
            individual_customer.dl_number = dlno
            individual_customer.insurance_company = insurancecompany
            individual_customer.policy_number = policyno
            individual_customer.save()
        else:
            employeeid = request.POST['employeeid']
            corporateid = request.POST['corporateid']

            corporate_customer = KprcCorporate()
            corporate_customer.cust = KprcCustomer.objects.get(cust_id = cust_id)
            corporate_customer.employee_id = employeeid
            corporate_customer.corporate = KprcCorporation.objects.get(corporate_id = corporateid)
            corporate_customer.save()



        cust_user = KprcCustUser()
        cust_user.cust_user_id = cust_id
        cust_user.cust_user_name = username
        cust_user.cust_user_password = password
        cust_user.save()


        return redirect('/customer_login')

    return render(request,'register.html', {'corporations': objs})



def customer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password =password  )

        if user is not None:
            auth.login(request , user)
            return redirect('/customerhome')
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/customer_login")
    else:
        return render(request,'customer_login.html')


def customerhome(request):
    d1 = datetime.now()
    aware_d1 = make_aware(d1)
    print(aware_d1)
    d2 = datetime.now()
    aware_d2 = make_aware(d2)
    print(aware_d2)
    print((aware_d2 - aware_d1).days)
    # new_d = d.replace(tzinfo=None)
    # print(new_d)

    # new_D = d.replace(hour=0, minute=0, second=0, microsecond=0)
    # print(new_D)
    # new_d = datetime.today()
    # print(new_d, 'PRINTING NEW DATE HAHAHAHAHAHhhhhh')
    # # midnight = datetime.time(0)
    #
    # new_date = datetime.combine(new_d, datetime.min())
    # print(new_date, 'PRINTING NEW DATE HAHAHAHAHAHhhhhh')


    print(request.user)
    username = request.user
    user = KprcCustUser.objects.get(cust_user_name = username)
    print(user.cust_user_id)
    return render(request, 'customerhome.html')




def starttrip(request):
    objs_locations = []
    objs_vehicles = []
    objs_daily_limit = 0
    selected_location = ''
    selected_vin = ''

    if request.method == 'GET':


        objs_locations = KprcLocation.objects.all()
        selected_location = request.GET.getlist('pickuplocation')
        print(selected_location)

        selected_classes = []
        selected_vehicles = []
        if selected_location:

            location_class = KprcLocationclass.objects.filter(location_id = selected_location[0])
            print(location_class)
            for entry in location_class:
                selected_classes.append(entry.class_field.class_id)
            print(selected_classes)



            for sc in selected_classes:

                selected_vehicle = KprcVehicle.objects.filter(class_field = sc)
                if selected_vehicle:
                    selected_vehicles.append(selected_vehicle[0])

            objs_vehicles = selected_vehicles

        selected_vin = request.GET.getlist('vin')

        if selected_vin:

            daily_limit_class = KprcVehicleclass.objects.get(class_id = KprcVehicle.objects.get(vin = int(selected_vin[0])).class_field.class_id)

            objs_daily_limit = daily_limit_class.daily_limit



    if selected_location:
        id = 0
        for locs in objs_locations:
            if locs.location_id == int(selected_location[0]):
                break
            id += 1


        temp = objs_locations[id]

        new_objs_locations = [temp]+objs_locations[:id]+objs_locations[id+1:]

    else:
        new_objs_locations = objs_locations




    if request.method == 'POST':


        username = request.user
        user = KprcCustUser.objects.get(cust_user_name=username)
        cust_id = user.cust_user_id


        rid = int(random.randint(1000, 9999))
        pickuplocation = request.GET['pickuplocation']
        dropofflocation = request.POST['dropofflocation']
        pickupdate = request.POST['pickupdate']
        print(pickupdate, 'PRINTING PICKUP DATE >>>>>>>>>>>>>>>>>>')
        # print(pickupdate.tzinfo)
        # print(datetime)
        startodometer = request.POST['startodometer']
        vin = request.GET['vin']

        daily_limit_class = KprcVehicleclass.objects.get(class_id=KprcVehicle.objects.get(vin=vin).class_field.class_id)
        dailylimit = daily_limit_class.daily_limit



        rental = KprcRentalService()
        rental.rental_service_id = rid
        rental.pickup_location = KprcLocation.objects.get(location_id = pickuplocation)
        rental.dropoff_location = KprcLocation.objects.get(location_id = dropofflocation)
        rental.pickup_date = pickupdate
        rental.dropoff_date = pickupdate
        rental.start_odometer = startodometer
        rental.end_odometer = 0
        rental.daily_limit = dailylimit
        rental.cust = KprcCustomer.objects.get(cust_id = cust_id)
        rental.vin = KprcVehicle.objects.get(vin = vin)
        rental.save()

        return redirect('/customerhome')

    return render(request, 'starttrip.html', {'locations': new_objs_locations, 'vehicles': objs_vehicles, 'selected_location': selected_location, 'daily_limit': objs_daily_limit})

def endtrip(request):

    # if request.method == 'GET':

    coupon_data = []

    total = 0

    username = request.user
    user = KprcCustUser.objects.get(cust_user_name=username)
    cust_id = user.cust_user_id
    rental_data = KprcRentalService.objects.filter(cust_id=cust_id, end_odometer = 0)

    d = datetime.now().date()
    # d = d.replace(tzinfo=None)
    print(d)
    print(cust_id, '>>>>>>>>>>>>>>>>>>>>>>>>>>')
    # corp_cust = KprcCorporate.objects.get(cust_id=KprcCustomer.objects.get(cust_id=cust_id))
    # corp_id = corp_cust.corporate_id
    # corp = KprcCorporation.objects.get(corporate_id=corp_id)
    # print(corp.discount)

    customer = KprcCustomer.objects.get(cust_id=cust_id)

    if customer.cust_type == 'kprc_individual':

        coupon_data = KprcCoupon.objects.filter(cust_id = KprcIndividual.objects.get(cust_id = KprcCustomer.objects.get(cust_id = cust_id)), validity__gte=d)
    # else:
    #     coupon



    if request.method == 'POST':
        dropoff = datetime.now()
        dropoffdate = make_aware(dropoff)
        # dropoffdate = dropoffdate.replace(tzinfo=None)
        endodometer = request.POST['endodometer']
        # endodometer = int(end_odometer)
        rid = request.GET['rental_service_id']
        if len(coupon_data) != 0:

            coupon_id = request.GET['coupon']
        else:
            coupon_id = ''



        rental = KprcRentalService.objects.get(rental_service_id = rid)
        rental.dropoff_date = dropoffdate
        rental.end_odometer = endodometer
        rental.save()
        # print(rental.pickup_date, rental.dropoff_date)
        # print((rental.dropoff_date-rental.pickup_date).days, 'PRINTING ..............>>>>>>>>>>>><<<<<<<<<<<!!!!!!!!!')


        # KprcVehicle.objects.get(vin=5690).vin


        # r = KprcVehicleclass.objects.get(class_id=KprcVehicle.objects.get(vin=rental.vin.vin).class_field.class_id)
        # rate = r.rental_rate
        # print(rate)

        r = KprcVehicleclass.objects.get(class_id=KprcVehicle.objects.get(vin=rental.vin.vin).class_field.class_id)
        rate = r.rental_rate
        over_fee = r.over_mileage_fee


        number_of_days = (rental.dropoff_date-rental.pickup_date).days
        odometer = int(rental.end_odometer) - int(rental.start_odometer)

        diff = odometer - (number_of_days)*rental.daily_limit

        if diff < 0:
            total = rate*number_of_days
        else:
            total = rate*number_of_days + diff*over_fee
        print(total)

        customer = KprcCustomer.objects.get(cust_id = cust_id)
        if customer.cust_type == 'kprc_individual':
            if coupon_id:
                coupon = KprcCoupon.objects.get(coupon_id = int(coupon_id))
                coupon_value = coupon.discount
                print(coupon_value)
                total -= total*(coupon_value/100)
                KprcCoupon.objects.filter(coupon_id = int(coupon_id)).delete()
            print(total)

        else:
            corp_cust = KprcCorporate.objects.get(cust_id=KprcCustomer.objects.get(cust_id=cust_id))
            corp_id = corp_cust.corporate_id
            corp = KprcCorporation.objects.get(corporate_id=corp_id)
            corporation_discount = corp.discount

            total -= total*(corporation_discount/100)
            print(total)

        rand_invoice = random.randint(100, 999)
        invoice_data = KprcInvoice()
        invoice_data.invoice_id = rand_invoice
        invoice_data.invoice_amount = total
        invoice_data.invoice_date = dropoffdate
        invoice_data.rental_service = KprcRentalService.objects.get(rental_service_id=rid)
        invoice_data.save()




        payment_method = request.POST['payment_method']
        card_number = request.POST['card_number']

        payment_d = datetime.now()
        payment_date = make_aware(payment_d)

        payment = KprcPayment()
        payment.payment_id = random.randint(100, 999)
        payment.payment_date = payment_date
        payment.payment_method = payment_method
        payment.card_number = card_number
        payment.invoice = KprcInvoice.objects.get(invoice_id = rand_invoice)
        payment.save()




    return render(request, 'endtrip.html', {'rental_data': rental_data, 'coupon_data': coupon_data, 'invoice': total})



def payment_page(request):



    return render(request, 'payment_page.html')



def allbookings(request):

    username = request.user
    user = KprcCustUser.objects.get(cust_user_name=username)
    cust_id = user.cust_user_id
    rental_data = KprcRentalService.objects.filter(cust_id = cust_id)




    return render(request, 'allbookings.html', {'rental_data': rental_data})









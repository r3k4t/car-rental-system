# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         # managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         # managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         # managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         # managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         # managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         # managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         # managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         # managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         # managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         # managed = False
#         db_table = 'django_session'


class KprcCorporate(models.Model):
    cust = models.OneToOneField('KprcCustomer', models.DO_NOTHING, primary_key=True)
    employee_id = models.IntegerField()
    corporate = models.ForeignKey('KprcCorporation', models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'kprc_corporate'


class KprcCorporation(models.Model):
    corporate_id = models.SmallIntegerField(primary_key=True)
    corporation_name = models.CharField(max_length=30)
    discount = models.SmallIntegerField()
    registration_number = models.BigIntegerField()

    class Meta:
        # managed = False
        db_table = 'kprc_corporation'


class KprcCoupon(models.Model):
    coupon_id = models.SmallIntegerField(primary_key=True)
    discount = models.SmallIntegerField()
    validity = models.DateTimeField()
    cust = models.ForeignKey('KprcIndividual', models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'kprc_coupon'


class KprcCustUser(models.Model):
    cust_user_id = models.SmallIntegerField()
    cust_user_name = models.CharField(max_length=20)
    cust_user_password = models.CharField(max_length=20)

    class Meta:
        # managed = False
        db_table = 'kprc_cust_user'


class KprcCustomer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_fname = models.CharField(max_length=20)
    cust_lname = models.CharField(max_length=20)
    cust_street = models.CharField(max_length=20)
    cust_city = models.CharField(max_length=15)
    cust_state = models.CharField(max_length=15)
    cust_email = models.CharField(max_length=30)
    cust_phone = models.BigIntegerField()
    cust_type = models.CharField(max_length=15)

    class Meta:
        # managed = True
        db_table = 'kprc_customer'


class KprcIndividual(models.Model):
    cust = models.OneToOneField(KprcCustomer, models.DO_NOTHING, primary_key=True)
    dl_number = models.CharField(max_length=30)
    insurance_company = models.CharField(max_length=30)
    policy_number = models.BigIntegerField()

    class Meta:
        # managed = False
        db_table = 'kprc_individual'


class KprcInvoice(models.Model):
    invoice_id = models.SmallIntegerField(primary_key=True)
    invoice_date = models.DateTimeField()
    invoice_amount = models.DecimalField(max_digits=9, decimal_places=2)
    rental_service = models.OneToOneField('KprcRentalService', models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'kprc_invoice'


class KprcLocation(models.Model):
    location_id = models.SmallIntegerField(primary_key=True)
    phone_number = models.BigIntegerField()
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'kprc_location'





class KprcPayment(models.Model):
    payment_id = models.SmallIntegerField(primary_key=True)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=30)
    card_number = models.BigIntegerField()
    invoice = models.ForeignKey(KprcInvoice, models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'kprc_payment'


class KprcRentalService(models.Model):
    pickup_location = models.ForeignKey(KprcLocation, models.DO_NOTHING, db_column='pickup_location', related_name='pickup')
    dropoff_location = models.ForeignKey(KprcLocation, models.DO_NOTHING, db_column='dropoff_location', related_name='dropoff')
    pickup_date = models.DateTimeField()
    dropoff_date = models.DateTimeField()
    start_odometer = models.IntegerField()
    end_odometer = models.IntegerField()
    daily_limit = models.IntegerField()
    cust = models.ForeignKey(KprcCustomer, models.DO_NOTHING)
    vin = models.ForeignKey('KprcVehicle', models.DO_NOTHING, db_column='vin')
    rental_service_id = models.FloatField(primary_key=True)

    class Meta:
        # managed = False
        db_table = 'kprc_rental_service'


class KprcVehicle(models.Model):
    vin = models.SmallIntegerField(primary_key=True)
    license_plate_number = models.CharField(max_length=20)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.DateTimeField()
    class_field = models.ForeignKey('KprcVehicleclass', models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.


    class Meta:
        # managed = False
        db_table = 'kprc_vehicle'


class KprcVehicleclass(models.Model):
    class_id = models.SmallIntegerField(primary_key=True)
    class_name = models.CharField(max_length=20)
    rental_rate = models.IntegerField()
    over_mileage_fee = models.IntegerField()
    daily_limit = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'kprc_vehicleclass'


class KprcLocationclass(models.Model):
    location = models.ForeignKey(KprcLocation, models.DO_NOTHING, db_column='location_id')
    class_field = models.ForeignKey(KprcVehicleclass, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.

    class Meta:
        # managed = False
        db_table = 'kprc_locationclass'
        unique_together = ('class_field', 'location')

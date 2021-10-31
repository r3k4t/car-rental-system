CREATE TABLE kprc_corporate (
    cust_id       SMALLINT NOT NULL COMMENT 'Customer Id',
    employee_id   INT NOT NULL COMMENT 'Employee Id of the customer',
    corporate_id  SMALLINT NOT NULL
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_corporate.cust_id IS
    'Customer Id'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_corporate.employee_id IS
    'Employee Id of the customer'; */

ALTER TABLE kprc_corporate ADD CONSTRAINT kprc_corporate_pk PRIMARY KEY ( cust_id );

CREATE TABLE kprc_corporation (
    corporate_id         SMALLINT NOT NULL COMMENT 'Corporate Id ',
    corporation_name     VARCHAR(30) NOT NULL COMMENT 'Corporation Name',
    discount             SMALLINT NOT NULL COMMENT 'Discount provided for the corporation',
    registration_number  BIGINT NOT NULL COMMENT 'Registration Number of the corporation'
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_corporation.corporate_id IS
    'Corporate Id '; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_corporation.corporation_name IS
    'Corporation Name'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_corporation.discount IS
    'Discount provided for the corporation'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_corporation.registration_number IS
    'Registration Number of the corporation'; */

ALTER TABLE kprc_corporation ADD CONSTRAINT kprc_corporation_pk PRIMARY KEY ( corporate_id );

CREATE TABLE kprc_coupon (
    coupon_id  SMALLINT NOT NULL COMMENT 'Id of the coupon',
    discount   SMALLINT NOT NULL COMMENT 'Percentage discount',
    validity   DATETIME NOT NULL COMMENT 'Validity Dates',
    cust_id    SMALLINT NOT NULL
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_coupon.coupon_id IS
    'Id of the coupon'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_coupon.discount IS
    'Percentage discount'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_coupon.validity IS
    'Validity Dates'; */

ALTER TABLE kprc_coupon ADD CONSTRAINT kprc_coupon_pk PRIMARY KEY ( coupon_id );

CREATE TABLE kprc_customer (
    cust_id      SMALLINT NOT NULL COMMENT 'Customer Id',
    cust_fname   VARCHAR(20) NOT NULL COMMENT 'First name of the customer',
    cust_lname   VARCHAR(20) NOT NULL COMMENT 'Last Name of the customer',
    cust_street  VARCHAR(20) NOT NULL COMMENT 'Street address of the customer',
    cust_city    VARCHAR(15) NOT NULL COMMENT 'City of the customer',
    cust_state   VARCHAR(15) NOT NULL COMMENT 'State of the customer',
    cust_email   VARCHAR(30) NOT NULL COMMENT 'Email of the customer',
    cust_phone   BIGINT NOT NULL COMMENT 'Phone number of customer',
    cust_type    VARCHAR(15) NOT NULL COMMENT 'Type of customer'
);

ALTER TABLE kprc_customer
    ADD CONSTRAINT ch_inh_kprc_customer CHECK ( cust_type IN ( 'KPRC_CORPORATE', 'KPRC_INDIVIDUAL' ) );

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_customer.cust_id IS
    'Customer Id'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_customer.cust_fname IS
    'First name of the customer'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_customer.cust_lname IS
    'Last Name of the customer'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_customer.cust_street IS
    'Street address of the customer'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_customer.cust_city IS
    'City of the customer'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_customer.cust_state IS
    'State of the customer'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_customer.cust_email IS
    'Email of the customer'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_customer.cust_phone IS
    'Phone number of customer'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_customer.cust_type IS
    'Type of customer'; */

ALTER TABLE kprc_customer ADD CONSTRAINT kprc_customer_pk PRIMARY KEY ( cust_id );

CREATE TABLE kprc_individual (
    cust_id            SMALLINT NOT NULL COMMENT 'Customer Id',
    dl_number          VARCHAR(30) NOT NULL COMMENT 'Driver License Number',
    insurance_company  VARCHAR(30) NOT NULL COMMENT 'Insurance company name',
    policy_number      BIGINT NOT NULL COMMENT 'Policy Number of insurance'
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_individual.cust_id IS
    'Customer Id'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_individual.dl_number IS
    'Driver License Number'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_individual.insurance_company IS
    'Insurance company name'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_individual.policy_number IS
    'Policy Number of insurance'; */

ALTER TABLE kprc_individual ADD CONSTRAINT kprc_individual_pk PRIMARY KEY ( cust_id );

CREATE TABLE kprc_invoice (
    invoice_id         SMALLINT NOT NULL COMMENT 'Id of the invoice',
    invoice_date       DATETIME NOT NULL COMMENT 'Date when invoice is generated',
    invoice_amount     DECIMAL(9, 2) NOT NULL COMMENT 'Amount in the invoice ',
    rental_service_id  DOUBLE NOT NULL
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_invoice.invoice_id IS
    'Id of the invoice'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_invoice.invoice_date IS
    'Date when invoice is generated'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_invoice.invoice_amount IS
    'Amount in the invoice '; */

CREATE UNIQUE INDEX kprc_invoice__idx ON
    kprc_invoice (
        rental_service_id
    ASC );

ALTER TABLE kprc_invoice ADD CONSTRAINT kprc_invoice_pk PRIMARY KEY ( invoice_id );

CREATE TABLE kprc_location (
    location_id   SMALLINT NOT NULL COMMENT 'Location Id',
    phone_number  BIGINT NOT NULL COMMENT 'Phone number of the location',
    street        VARCHAR(30) NOT NULL COMMENT 'Street address of the location',
    city          VARCHAR(20) NOT NULL COMMENT 'City of the location',
    state         VARCHAR(20) NOT NULL COMMENT 'State of the location',
    zipcode       INT NOT NULL COMMENT 'Zipcode of the location'
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_location.location_id IS
    'Location Id'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_location.phone_number IS
    'Phone number of the location'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_location.street IS
    'Street address of the location'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_location.city IS
    'City of the location'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_location.state IS
    'State of the location'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_location.zipcode IS
    'Zipcode of the location'; */

ALTER TABLE kprc_location ADD CONSTRAINT kprc_location_pk PRIMARY KEY ( location_id );

CREATE TABLE kprc_locationclass (
    location_id  SMALLINT NOT NULL,
    class_id     SMALLINT NOT NULL
);

ALTER TABLE kprc_locationclass ADD CONSTRAINT kprc_locationclass_pk PRIMARY KEY ( class_id,
                                                                                  location_id );

CREATE TABLE kprc_payment (
    payment_id      SMALLINT NOT NULL COMMENT 'Id of the payment',
    payment_date    DATETIME NOT NULL COMMENT 'Date of the payment',
    payment_method  VARCHAR(30) NOT NULL COMMENT 'Method of the payment',
    card_number     BIGINT NOT NULL COMMENT 'Card number used in the payment',
    invoice_id      SMALLINT NOT NULL
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_payment.payment_id IS
    'Id of the payment'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_payment.payment_date IS
    'Date of the payment'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_payment.payment_method IS
    'Method of the payment'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_payment.card_number IS
    'Card number used in the payment'; */

ALTER TABLE kprc_payment ADD CONSTRAINT kprc_payment_pk PRIMARY KEY ( payment_id );

CREATE TABLE kprc_rental_service (
    pickup_location    SMALLINT NOT NULL COMMENT 'Pickup location of the vehicle',
    dropoff_location   SMALLINT NOT NULL COMMENT 'Dropoff location of the vehicle',
    pickup_date        DATETIME NOT NULL COMMENT 'Date of the pickup',
    dropoff_date       DATETIME NOT NULL COMMENT 'Date of dropoff',
    start_odometer     INT NOT NULL COMMENT 'Odometer reading at the start',
    end_odometer       INT NOT NULL COMMENT 'Odometer reading at the end',
    daily_limit        INT NOT NULL COMMENT 'Daily Odometer Limit',
    cust_id            SMALLINT NOT NULL,
    vin                SMALLINT NOT NULL,
    rental_service_id  DOUBLE NOT NULL
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_rental_service.pickup_location IS
    'Pickup location of the vehicle'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_rental_service.dropoff_location IS
    'Dropoff location of the vehicle'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_rental_service.pickup_date IS
    'Date of the pickup'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_rental_service.dropoff_date IS
    'Date of dropoff'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_rental_service.start_odometer IS
    'Odometer reading at the start'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_rental_service.end_odometer IS
    'Odometer reading at the end'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_rental_service.daily_limit IS
    'Daily Odometer Limit'; */

ALTER TABLE kprc_rental_service ADD CONSTRAINT kprc_rental_service_pk PRIMARY KEY ( rental_service_id );

CREATE TABLE kprc_vehicle (
    vin                   SMALLINT NOT NULL COMMENT 'Vehicle Identification Number',
    license_plate_number  VARCHAR(20) NOT NULL COMMENT 'License Plate Number',
    make                  VARCHAR(30) NOT NULL COMMENT 'Make of the vehicle',
    model                 VARCHAR(30) NOT NULL COMMENT 'Model of the vehicle',
    year                  DATETIME NOT NULL COMMENT 'Year of manufacture of the vehicle',
    class_id              SMALLINT NOT NULL
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_vehicle.vin IS
    'Vehicle Identification Number'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_vehicle.license_plate_number IS
    'License Plate Number'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_vehicle.make IS
    'Make of the vehicle'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_vehicle.model IS
    'Model of the vehicle'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_vehicle.year IS
    'Year of manufacture of the vehicle'; */

ALTER TABLE kprc_vehicle ADD CONSTRAINT kprc_vehicle_pk PRIMARY KEY ( vin );

CREATE TABLE kprc_vehicleclass (
    class_id          SMALLINT NOT NULL COMMENT 'Id of the class of vehicle',
    class_name        VARCHAR(20) NOT NULL COMMENT 'Name of the class',
    rental_rate       INT NOT NULL COMMENT 'Rental rate per day for the class',
    over_mileage_fee  INT NOT NULL COMMENT 'Over mileage fee for the class'
);

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_vehicleclass.class_id IS
    'Id of the class of vehicle'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_vehicleclass.class_name IS
    'Name of the class'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_vehicleclass.rental_rate IS
    'Rental rate per day for the class'; */

/* Moved to CREATE TABLE
COMMENT ON COLUMN kprc_vehicleclass.over_mileage_fee IS
    'Over mileage fee for the class'; */

ALTER TABLE kprc_vehicleclass ADD CONSTRAINT kprc_vehicleclass_pk PRIMARY KEY ( class_id );

ALTER TABLE kprc_corporate
    ADD CONSTRAINT corporate_corporation_fk FOREIGN KEY ( corporate_id )
        REFERENCES kprc_corporation ( corporate_id );

ALTER TABLE kprc_corporate
    ADD CONSTRAINT corporate_customer_fk FOREIGN KEY ( cust_id )
        REFERENCES kprc_customer ( cust_id );

ALTER TABLE kprc_coupon
    ADD CONSTRAINT individual_coupon_fk FOREIGN KEY ( cust_id )
        REFERENCES kprc_individual ( cust_id );

ALTER TABLE kprc_individual
    ADD CONSTRAINT individual_customer_fk FOREIGN KEY ( cust_id )
        REFERENCES kprc_customer ( cust_id );

ALTER TABLE kprc_invoice
    ADD CONSTRAINT invoice_rental_service_fk FOREIGN KEY ( rental_service_id )
        REFERENCES kprc_rental_service ( rental_service_id );

ALTER TABLE kprc_locationclass
    ADD CONSTRAINT locationclass_class_fk FOREIGN KEY ( class_id )
        REFERENCES kprc_vehicleclass ( class_id );

ALTER TABLE kprc_locationclass
    ADD CONSTRAINT locationclass_location_fk FOREIGN KEY ( location_id )
        REFERENCES kprc_location ( location_id );

ALTER TABLE kprc_payment
    ADD CONSTRAINT payment_invoice_fk FOREIGN KEY ( invoice_id )
        REFERENCES kprc_invoice ( invoice_id );

ALTER TABLE kprc_rental_service
    ADD CONSTRAINT rental_customer_fk FOREIGN KEY ( cust_id )
        REFERENCES kprc_customer ( cust_id );

ALTER TABLE kprc_rental_service
    ADD CONSTRAINT rental_dropofflocation_fk FOREIGN KEY ( dropoff_location )
        REFERENCES kprc_location ( location_id );

ALTER TABLE kprc_rental_service
    ADD CONSTRAINT rental_invoice_fk FOREIGN KEY ( pickup_location )
        REFERENCES kprc_location ( location_id );

ALTER TABLE kprc_rental_service
    ADD CONSTRAINT rental_vehicle_fk FOREIGN KEY ( vin )
        REFERENCES kprc_vehicle ( vin );

ALTER TABLE kprc_vehicle
    ADD CONSTRAINT vehicle_class_fk FOREIGN KEY ( class_id )
        REFERENCES kprc_vehicleclass ( class_id );


CREATE TABLE kprc_cust_user (
    cust_user_id      SMALLINT NOT NULL COMMENT 'Customer Id',
    cust_user_name   VARCHAR(20) NOT NULL COMMENT 'Username of the customer',
    cust_user_password  VARCHAR(20) NOT NULL COMMENT 'Password of the customer'
);
        

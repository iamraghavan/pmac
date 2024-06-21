from django.db import models

class Profiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_pmid = models.CharField(unique=True, max_length=255)
    age = models.IntegerField(blank=True, null=True)
    profile_image = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    religion = models.CharField(max_length=255, blank=True, null=True)
    mother_tongue = models.CharField(max_length=255, blank=True, null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(max_length=255, blank=True, null=True)
    disability = models.CharField(max_length=255, blank=True, null=True)
    family_status = models.CharField(max_length=255, blank=True, null=True)
    family_type = models.CharField(max_length=255, blank=True, null=True)
    family_value = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    employed_in = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    annual_income = models.CharField(max_length=255, blank=True, null=True)
    work_location = models.CharField(max_length=255, blank=True, null=True)
    residing_state = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    horoscope_url = models.TextField(blank=True, null=True)
    my_bio = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles'

class UserPayments(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_pmid = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    package_details = models.CharField(max_length=255)
    paid_status = models.IntegerField()
    date_of_paid = models.DateTimeField(blank=True, null=True)
    plan_expired_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_payments'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    pmid = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    phone = models.CharField(unique=True, max_length=255)
    gender = models.CharField(max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


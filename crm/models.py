from django.db import models
from django.utils import timezone
import mathfilters
from django.conf import settings


# Create your models here.
class Customer(models.Model):
    cust_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    bldgroom = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=10)
    organization = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.cust_name


class Service(models.Model):
    cust_name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='services')
    service_category = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=200)
    setup_time = models.DateTimeField(
        default=timezone.now)
    cleanup_time = models.DateTimeField(
        default=timezone.now)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.cust_name)


class Product(models.Model):
    cust_name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='products')
    product = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    pickup_time = models.DateTimeField(
        default=timezone.now)
    charge = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.cust_name)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

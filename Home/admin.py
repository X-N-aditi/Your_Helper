from django.contrib import admin
from .models import Customer, ServiceProvider

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age', 'phone_number', 'address', 'state', 'city', 'pincode', 'created_at']


@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'service', 'title', 'age', 'dob', 'phone_number', 'address', 'state', 'city', 'pincode', 'identity_proof', 'year_of_experience', 'experience_certificate', 'photo', 'created_at']

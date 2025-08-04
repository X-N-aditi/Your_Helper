from django.db import models
import uuid

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=500)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name and self.email


class ServiceProvider(models.Model):

    IDENTITY_CHOICES = [
        ('adhaar-card', 'Adhaar Card'),
        ('pan-card', 'Pan Card'),
        ('votar-id-card', 'Votar ID Card'),
    ]

    SERVICE_CHOICES = [
        ('electrician', 'Electrician'),
        ('sweeper', 'Sweeper'),
        ('cleaner', 'Cleaner'),
        ('cook', 'Cook'),
        ('gardener', 'Gardener'),
        ('plumber', 'Plumber'),
        ('mechanic', 'Mechanic'),
        ('beautician', 'Beautician'),
        ('mistary', 'Mistary')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    title = models.CharField(max_length=100, blank=False, null=False)
    service_charge = models.DecimalField(max_digits=8, decimal_places=2, default=900.0)
    service_duration = models.PositiveIntegerField(default=30)
    age = models.PositiveIntegerField()
    dob = models.DateField()
    phone_number = models.PositiveIntegerField()
    address = models.CharField(max_length=500)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.PositiveIntegerField()
    identity_proof = models.CharField(max_length=20, choices=IDENTITY_CHOICES)
    year_of_experience = models.PositiveIntegerField(blank=True, null=True)
    experience_certificate = models.FileField(upload_to='certificates/', blank=True, null=True)
    photo = models.ImageField(upload_to='service_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service} - {self.title} - {self.service_charge} - {self.service_duration}"
    


class Booking(models.Model):
    booking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, related_name='service_provider')
    service_date = models.DateField(auto_now_add=True)
    address = models.TextField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.customer} - {self.booking_id}


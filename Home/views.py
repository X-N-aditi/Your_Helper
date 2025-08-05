from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerForm, ServiceProviderForm, LoginForm
from .models import ServiceProvider, Customer, Booking

def home(request):
    return render(request, 'home/home.html')

def Sign_login_page(request):
    return render(request, 'home/Sign_Login.html')

def signup_choice_view(request):
    return render(request, 'home/signup_choice.html')


def Customer_sign_up(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomerForm()
    return render(request, 'home/register_customer.html', {'form':form})

def Service_provider_sign_up(request):
    if request.method == 'POST':
        form = ServiceProviderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ServiceProviderForm()
    return render(request, 'home/register_service_provider.html', {'form':form})




def login_view(request):
    next_url = request.GET.get('next')  

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Check Customer model
            customer = Customer.objects.filter(email=email).first()
            if customer:
                request.session['user_id'] = customer.id
                request.session['user_type'] = 'customer'
                return redirect(next_url or 'home')  

            # Check ServiceProvider model
            provider = ServiceProvider.objects.filter(email=email).first()
            if provider:
                request.session['user_id'] = provider.id
                request.session['user_type'] = 'provider'
                return redirect(next_url or 'home')  

            form.add_error('email', 'No account found with this email.')
    else:
        form = LoginForm()

    return render(request, 'home/login.html', {'form': form})




def service_by_role(request, service):
    providers = ServiceProvider.objects.filter(service=service.lower())
    return render(request, 'home/service_role.html', {
        'providers': providers,
        'role': service.capitalize(),
    })




def book_service(request, provider_id):
    if not request.session.get('user_id') or request.session.get('user_type') != 'customer':
        return redirect(f'/login/?next=/book/{provider_id}/')  

    customer_id = request.session.get('user_id')
    customer = get_object_or_404(Customer, id=customer_id)
    provider = get_object_or_404(ServiceProvider, id=provider_id)

    if request.method == 'POST':
        address = request.POST.get('address')
        if address:
            booking = Booking.objects.create(
                customer=customer,
                service_provider=provider,
                address=address
            )
            return redirect('dummy-payment', booking_id=booking.booking_id)
    
    return render(request, 'home/book_service.html', {'provider': provider})


def dummy_payment(request, booking_id):
    booking = get_object_or_404(Booking, booking_id=booking_id)
    return render(request, 'home/payment.html', {'booking': booking})




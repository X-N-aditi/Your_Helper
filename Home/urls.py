from django.urls import path
from .views import Sign_login_page, Customer_sign_up, Service_provider_sign_up, signup_choice_view, login_view, home, service_by_role, book_service, dummy_payment

urlpatterns = [
    path('', home, name='home'),
    path('Sign_login_page/', Sign_login_page, name='signup/login'),
    path('signup/', signup_choice_view, name='signup-choice'),
    path('register/customer/', Customer_sign_up, name='customer-signup'),
    path('register/provider/', Service_provider_sign_up, name='service-provider-signup'),
    path('login/', login_view, name='login'),
    path('service/<str:service>/', service_by_role, name='service-by-role'),
    path('book/<int:provider_id>/', book_service, name='book-service'),
    path('payment/<uuid:booking_id>/', dummy_payment, name='dummy-payment'),


]


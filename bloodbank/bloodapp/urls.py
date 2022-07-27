from django.urls import path
from .views import *

urlpatterns = [
    path('signin/', sign_in, name='signin'),
    path('register/', registerview, name='new'),
    path('search/', blood_search, name='search'),    #search
    path('datas/', blood_records, name='datas'),
    path('newpage/', newpage, name='forgot'),
    path('homepage/', homepage),
    path('login/', log_in, name='login'),     #login
]
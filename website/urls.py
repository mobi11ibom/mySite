from django.urls import path
from website.views import *

urlpatterns = [
    path('', home_view),       # برای آدرس اصلی: http://127.0.0.1:8000/
   path('home' , home_view),
   path('contact',contact_view),
   path('about',about_view)

]

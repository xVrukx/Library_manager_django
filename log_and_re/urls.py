from django.urls import path
from log_and_re.views import *

urlpatterns = [
    path('', Register, name='register'),
]
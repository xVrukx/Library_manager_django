
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('log_and_re.urls')),
    path('Library', include('Library.urls'))
]

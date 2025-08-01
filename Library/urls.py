from django.urls import path
from Library.views import *

urlpatterns = [
    path('Library/', Library, name='Library'),
    path('add-member/', add_member, name='add_member'),
    path('add-book/', add_book, name='add_book'),
    path('borrow-return/',borrow_and_return, name='borrow_and_return'),
]
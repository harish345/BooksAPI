'''
Created on June 29, 2019

@author: harish345
'''
from django.urls import path
import booksapi.views as views

urlpatterns  = [
    path('v1/books',views.BooksList.as_view(), name="listCreate"),
    path('v1/books/<id>',views.BooksList.as_view(),name="getUpdateDelete"),
    path('external-books',views.list_external_books, name="external_books"),
    ]
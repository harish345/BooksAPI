"""
Created on June 29, 2019

@author: harish345

"""

from django.test import TestCase, Client
from django.urls import reverse
from booksapi.models import Books
from booksapi.serializers import BookSerializer
from rest_framework import status
import json

client = Client()
# Create your tests here.
class BookApiTest(TestCase):
    
    def setUp(self):
        self.update_book = Books.objects.create(name= "testPatch",isbn="153-765",
            authors=["testAuth"],release_date= "2019-04-15",country="India",number_of_pages=500,publisher="testPatchPub")
        self.get_book = Books.objects.create(name= "testGet",isbn="153-7650",
            authors=["testAuth"],release_date= "2019-04-15",country="India",number_of_pages=500,publisher="testGetPub")
        self.valid_payload_post = {
                    "name": "testCreate",
                    "isbn": "14378-88701",
                    "authors": [
                            "testautCreate"
                            ],
                    "country": "india",
                    "number_of_pages": 600,
                    "publisher": "tetspubCreate",
                    "release_date": "2019-06-30"
                    }
        self.invalid_payload_post = {
                "name": "testCreate_invalid",
                "isbn": "14378-88601",
                "country": "india",
                "number_of_pages": 600,
                "publisher": "tetspubCreate",
                "release_date": "2019-06-30"
                }
        self.payload_patch = {
                "isbn": "14378-88731",
                "number_of_pages": 600,
                "publisher": "tetspubPatch",
                }
       
    def test_create_valid_book(self):
        response = client.post(
            reverse('listCreate'),
            data=json.dumps(self.valid_payload_post),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_book(self):
        response = client.post(
            reverse('listCreate'),
            data=json.dumps(self.invalid_payload_post),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_valid_update_book(self):
        response = client.patch(
            reverse('getUpdateDelete', kwargs={'id': self.update_book.id}),
            data=json.dumps(self.payload_patch),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_book(self):
        response = client.patch(
            reverse('getUpdateDelete', kwargs={'id': 88}),
            data=json.dumps(self.payload_patch),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
       
    def test_get_valid_book(self):
        response = client.get(
            reverse('getUpdateDelete', kwargs={'id': self.get_book.id}))
        book = Books.objects.get(id=self.get_book.id)
        serializer = BookSerializer(book)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_book(self):
        response = client.get(
            reverse('getUpdateDelete', kwargs={'id': 99}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_delete_valid_book(self):
        response = client.delete(
            reverse('getUpdateDelete', kwargs={'id': self.get_book.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_invalid_book(self):
        response = client.delete(
            reverse('getUpdateDelete', kwargs={'id': 99}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_get_all_books(self):
        response = client.get(reverse('listCreate'))
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_book_external(self):
        response = client.get(reverse('external_books'),{'name':'A Game of Thrones'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_invalid_book_external(self):
        response = client.get(reverse('external_books'),{'name':'Game of Thrones'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
"""
Created on June 29, 2019

@author: harish345

View module for Books Api. Provides GET,POST,PATCH,DELETE methods

"""

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
import requests
from .models import Books
from .serializers import BookSerializer
from booksapi.Utils import build_response,build_external_book_response
import logging

# Get an instance of a logger
log = logging.getLogger(__name__)


class BooksList(APIView):
    """
    List all books, or create a new book ,or update a book, or delete a book.
    """
    def get(self, request ,id=None):
        """
        List all books.
        """
        try:
            if id==None:
                books = Books.objects.all()
                book_serializer = BookSerializer(books, many=True)
            elif id !=None and Books.objects.filter(id=id).first():
                book = Books.objects.get(id=id)
                book_serializer = BookSerializer(book)
            else:
                return Response(build_response("error", 404, [],"The book with id:"+id+" not available."),status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error": "Internal server error. Please try again later"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(build_response("success", 200, book_serializer.data),status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a new book.
        """
        try:
            book_serializer = BookSerializer(data=request.data)
            if book_serializer.is_valid():
                book_serializer.save()
                response = build_response("success", 200, [{"book":book_serializer.data}])
                log.info('Book '+book_serializer.data['name']+' created successfully')
                return Response(response,status=status.HTTP_201_CREATED)
            else:
                log.error(book_serializer.errors)
                return Response(build_response("error", 400, book_serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error": "Internal server error. Please try again later"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    def patch(self, request ,id):
        """
        Update a book.
        """
        try:
            book = Books.objects.filter(id=id).first()
            if book:
                book_serializer = BookSerializer(book)
                book_serializer.update(book, request.data)
                log.info('The book '+book.name+' updated successfully')
            else:
                log.info("The book with id:"+id+" not available.")
                return Response(build_response("error", 404, [],"The book with id:"+id+" not available."),status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error": "Internal server error. Please try again later"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(build_response("success", 200, book_serializer.data,"The book "+book.name+" was updated successfuly."),status=status.HTTP_200_OK)

    def delete(self, request ,id):
        """
        Delete a book.
        """
        try:
            book = Books.objects.filter(id=id).first()
            if book:
                book_name=book.name
                book.delete()
                log.info("The book "+book_name+" was deleted successfuly.")
            else:
                log.info("The book with id:"+id+" not available.")
                return Response(build_response("error", 404, [],"The book with id:"+id+" not available."),status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error": "Internal server error. Please try again later"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(build_response("success", 200, [],"The book "+book_name+" was deleted successfuly."),status=status.HTTP_200_OK)



@api_view(['GET'])
def list_external_books(request):
    """
    Get books from by querying the Ice And Fire API
    """
    url = "https://www.anapioficeandfire.com/api/books"
    response={}
    try:
        q = request.GET.get('name',None)
        params = {'name':q}
        data = requests.get(url,params=params)
        response_json = data.json()
        response = build_external_book_response(response_json)
        return Response(response,status=status.HTTP_200_OK)
    except Exception as e:
        log.error(e)
        return Response({"Error": "Internal server error. Please try again later"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
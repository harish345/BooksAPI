"""
Created on June 29, 2019

@author: harish345

"""
from rest_framework import serializers
from booksapi.models import Books

# Serializer class for Books model
class BookSerializer(serializers.ModelSerializer):
    authors = serializers.ListField(child=serializers.CharField())
    class Meta:
        model=Books
        fields = ('id','name','isbn','authors','country','number_of_pages','publisher','release_date')
    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.authors = validated_data.get('authors', instance.authors)
        instance.country = validated_data.get('country', instance.country)
        instance.number_of_pages = validated_data.get('number_of_pages', instance.number_of_pages)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.save()
        return instance
        
class ResponseSerializer(serializers.Serializer):
    status_code = serializers.IntegerField()
    status = serializers.CharField()
    message = serializers.CharField()
    data = serializers.ListField(child=serializers.JSONField())
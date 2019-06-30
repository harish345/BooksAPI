'''
Created on June 29, 2019

@author: harish345
'''

from .serializers import ResponseSerializer

def build_response(status,status_code,data,message=None):
    if message!=None:
        response_object = {"status": status,"status_code":status_code,"message":message,"data":data}
    else:
        response_object = {"status": status,"status_code":status_code,"data":data}
    response = ResponseSerializer(data=response_object)
    response.is_valid()
    return response.data


def build_external_book_response(response_json):
    external_response = []
    for book_data in response_json:
        response = {}
        response["name"] = book_data["name"]
        response["isbn"] = book_data["isbn"]
        response["authors"] = book_data["authors"]
        response["country"] = book_data["country"]
        response["number_of_pages"] = book_data["numberOfPages"]
        response["publisher"] = book_data["publisher"]
        response["release_date"] = book_data["released"][0:10]
        external_response.append(response)
    return build_response("success", 200,external_response)
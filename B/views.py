from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from B.models import B_Database_Model_ORM_Schema
import json

def ViewsB(request):
    #Access models from here
    data = list(B_Database_Model_ORM_Schema.objects.filter(id=1).values(
        "test1",
        "test2",
        "test3",
        "test4",
        "test5",
        "test6",
        "test7",
        "test8",
        "test9",
        "test10"
    ))
    data = json.loads(json.dumps(data)) #Serialization. Native serialization is more reliable than Django Serializers

    return HttpResponse("Hello From B")
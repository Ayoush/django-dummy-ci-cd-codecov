from django.shortcuts import render
from testcases.serializers import OrgSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from testcases import serializers
from .models import Org

@api_view(['GET'])
def org_index(request):
    orgs = Org.objects.all()
    serializer = OrgSerializer(orgs, many=True)
    return Response(serializer.data)    

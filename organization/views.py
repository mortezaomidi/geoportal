from rest_framework import generics, serializers

from .models import Organization
from .serializers import OrganizationModelSerializer


class OrganizationList(generics.ListCreateAPIView):
    
    queryset = Organization.objects.all()
    seriilizer_class = OrganizationModelSerializer
    

class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Organization.objects.all()
    serializer_class = OrganizationModelSerializer
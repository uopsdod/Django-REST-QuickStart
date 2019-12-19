from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import UserSerializer, GroupSerializer

# ViewSet in Django is like 'Resources' or 'Controllers'
# https://www.django-rest-framework.org/api-guide/viewsets/

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profile to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProfileViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for profile.
    """
    def list(self, request):
        # queryset = User.objects.all()
        # serializer = UserSerializer(queryset, many=True)
        tmpstr = {
            'key001':'val001',
            'key002':'val002'
        }
        return Response(tmpstr)



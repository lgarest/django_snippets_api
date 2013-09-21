from rest_framework import generics
from rest_framework import permissions

from ..models import Snippet
from ..serializers import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User


class SnippetList(generics.ListCreateAPIView):
    """
    Snippet listing view as a class using generics methods and adding a snippet owner.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def pre_save(self, obj):
        obj.owner = self.request.user


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Snippet detail view as a class using generics methods and adding a snippet owner.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def pre_save(self, obj):
        obj.owner = self.request.user

# v4_0 and further
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

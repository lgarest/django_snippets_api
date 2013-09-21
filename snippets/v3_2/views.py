from rest_framework import generics

from ..models import Snippet
from ..serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    """Snippet listing view as a class using generics methods"""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """Snippet detail view as a class using generics methods"""

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

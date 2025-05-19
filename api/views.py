from django.shortcuts import render
from .models import Blogpost
# Create your views here.
# Django restframework views
from rest_framework import generics
from .serializers import BlogPostSerializer
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogPostSerializer
    


class BlogPostRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset= Blogpost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"
    
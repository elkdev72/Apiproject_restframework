from rest_framework import serializers
from .models import Blogpost,Users

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = ['id','title',"content","published_date"]


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['name','age']
from django.shortcuts import render
from django.http import JsonResponse

# Third party imports
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post
from rest_framework import permissions, generics, mixins
#from rest_framework.permissions import IsAuthenticated


class PostView(mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    # there are 2 ways of specifying serializer class - serializer_class or get_serializer_class
    # (if you want to specify different classes for get and post then method can be used)
    serializer_class = PostSerializer
    # there are 2 ways of specifying queryset - queryset or get_queryset method
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class TestView(APIView):
    # using http JsonResponse
    """def test_view(request):
    data={
        'name':'harshita',
        'age':24
    }
    return JsonResponse(data)"""
    # using rest framework response
    """def get(self, request, *args, **kwargs):
        data={
            'name':'harshita',
            'age':24
        }
        return Response(data)"""
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = (IsAuthenticated,)
    # using serializer to return JSON response
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        # many = True as we are getting multiple instances of Post
        serializer1 = PostSerializer(qs, many=True)
        return Response(serializer1.data)

    """ check if the request to the API is correct or not 
    (request is in properly serialized as per our serialization or not)"""

    # we need to see if the request data matches the serializer data
    def post(self, request, *args, **kwargs):
        # data keyword in param means you want to check if the request is valid or not
        serializer1 = PostSerializer(data = request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data)
        else:
            return Response(serializer1.errors)
    
    def __str__(self):
        self.owner.name
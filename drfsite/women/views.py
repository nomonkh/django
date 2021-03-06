from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({'posts':
                             list(lst)})

    def post(self, request):
        post_new    = Women.object.create(
            title   = request.data['title'],
            content = request.data['content'],
            cat_id  = request.data['cat_id']
        )
        return Response({'posts': model_to_dict(post_new)})
# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

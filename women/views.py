from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.authentication import *
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from .models import *
from .permissions import *
from .serializers import *


# Create your views here.
def index(request):
    return HttpResponse('Hello, World!')


class WomenAPIPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100000


class WomenViewSet(viewsets.ModelViewSet):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes = (IsAdminOrReadOnly, IsOwnerOrReadOnly, )
    # authentication_classes = (TokenAuthentication, SessionAuthentication, )
    permission_classes = (IsAuthenticated, )
    pagination_class = WomenAPIPagination

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            # return Women.objects.all()[:3]
            return Women.objects.all()

        return Women.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})


# class WomenAPIListCreate(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIView2(APIView):
#     def get(self, request):
#         # query_set = Women.objects.all().values()
#         query_set = Women.objects.all()
#         return Response({"posts": WomenSerializer(query_set, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method Delete not allowed."})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist."})
#         instance.delete()
#         return Response({"deleted data": str(pk)})
#         # data = get_object_or_404(Women, id=request.data['id'])
#         # data.delete()
#         # return Response(model_to_dict(data))
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method Put not allowed."})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists."})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#         # data = Women.objects.get(id=request.data['id'])
#         # data.title = request.data['title']
#         # data.time_updated = timezone.now()
#         # data.save()
#         # return Response(model_to_dict(data))

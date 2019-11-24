from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Counsellor
from rest_framework import generics, status
from . import serializers
from .serializers import ConsSerializer
from rest_framework import viewsets

from rest_framework.generics import get_object_or_404

# Create your views here.


class Cons(viewsets.ViewSet):
    serializer_class = ConsSerializer
    queryset = Counsellor.objects.all()
 
    def list(self, request):
        queryset = Counsellor.objects.all()
        serializer = ConsSerializer(queryset,many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = Counsellor.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ConsSerializer(user)
        return Response(serializer.data)
    def get(self,request):

        counsellors = Counsellor.objects.all()

        serializer = serializers.ConsSerializer(counsellors,many=True)
        return Response({'counsellors':serializer.data})

    def newname(self, request):
        counsellor = request.data.get('counsellor')
        serializer = serializers.ConsSerializer(data=counsellor)
        if serializer.is_valid(raise_exception=True):
            counsellor_saved = serializer.save()
        # return Response({"counsellor '{}'".format(counsellor_saved.title)})
        return HttpResponse('<div>{}</div>'.format(counsellor_saved.title))
    def delete(self, request, pk):
        counsellor = get_object_or_404(Counsellor.objects.all(), pk=pk)
        counsellor.delete()
        return Response({
            "message": "counsellor with id `{}` has been deleted.".format(pk)
        }, status=204)

    def create(self, request, *args, **kwargs):
        name= request.data.get('name')
        secret_key = request.data.get('secret_key')
        lists = request.data.get('lists')
        timetable = request.data.get('timetable')
        id = request.data.get('id')

        counsellor = Counsellor.create(name=name,secret_key=secret_key,lists=lists,timetable=timetable) #нада чета исправить но нинаю что
        counsellor.save()
        #counsellor.create()

        return Response({
            "message": "counsellor with id `{}` has been created.".format(111)
        }, status=201)
#        try:
#            return super(ConsCreateView, self).create(request, args, kwargs)
#        except:
#            return Response({'counsellors': 'че за ошибка блин!!!!'})
#        else:
#            response = {"status_code": status.HTTP_201_CREATED,
#                        "message": "Successfully created",
#                        "result": request.data}
#            return Response(response)        


#class Cons(APIView):

    #def get(self,request):
#
    #    counsellors = Counsellor.objects.all()
#
    #    serializer = serializers.ConsSerializer(counsellors,many=True)
    #    return Response({'counsellors':serializer.data})
#
#
    #def newname(self, request):
    #    counsellor = request.data.get('counsellor')
    #    serializer = serializers.ConsSerializer(data=counsellor)
    #    if serializer.is_valid(raise_exception=True):
    #        counsellor_saved = serializer.save()
    #    return Response({"counsellor '{}'".format(counsellor_saved.title)})
#
    #def delete(self, request, pk):
    #    counsellor = get_object_or_404(Counsellor.objects.all(), pk=pk)
    #    counsellor.delete()
    #    return Response({
    #        "message": "counsellor with id `{}` has been deleted.".format(pk)
    #    }, status=204)
        


#class ConsCreateView(generics.CreateAPIView):
#    queryset = Counsellor.objects.all()
#    serializer_class = serializers.ConsSerializer
#
#    def create(self, request, *args, **kwargs):
#        try:
#            return super(ConsCreateView, self).create(request, args, kwargs)
#        except:
#            return Response({'counsellors': 'че за ошибка блин!!!!'})
#        else:
#            response = {"status_code": status.HTTP_201_CREATED,
#                        "message": "Successfully created",
#                        "result": request.data}
#            return Response(response)
#


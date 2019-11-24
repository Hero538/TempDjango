from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from .models import News
from .serializers import NewsSerializer
from rest_framework.generics import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView

# Create your views here.

class News_cs(ListModelMixin, GenericAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.request.data.get('user_id'))
        return serializer.save(user=user)

class UpdateNews(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Counsellor


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counsellor
        fields = ('name','user','secret_key','lists','timetable')


class ConsSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=128)
    secret_key = serializers.CharField(max_length=128)
    lists = serializers.CharField()
    timetable = serializers.CharField()

    def createcons(self, validated_data):
        return Counsellor.objects.create(**validated_data)

    def updatecons(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.secret_key = validated_data.get('secret_key', instance.secret_key)
        instance.lists = validated_data.get('lists', instance.lists)
        instance.timetable = validated_data.get('timetable', instance.timetable)
        instance.save()
        return instance


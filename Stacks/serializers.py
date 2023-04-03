from Stacks import models
from rest_framework import serializers
from  Stacks.models import Django



class DjangoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Django
        fields=['id','title','content','progress']


class NodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Django
        fields=['id','title','content','progress']


class ReactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Django
        fields=['id','title','content','progress']  

class UiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Django
        fields=['id','title','content','progress']   



class laravelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Django
        fields=['id','title','content','progress']                     



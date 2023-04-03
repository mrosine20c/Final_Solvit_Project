from Stacks import models
from rest_framework import serializers
from  Stacks.models import DjangoModel, Node,React,Ui_ux,Laravel



class DjangoSerializer(serializers.ModelSerializer):

    class Meta:
        model = DjangoModel
        fields=['id','title','content','progress']


class NodeSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Node
        fields=['id','title','content','progress']


class ReactSerializer(serializers.ModelSerializer):

    class Meta:
        model = React
        fields=['id','title','content','progress']  

class UiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ui_ux
        fields=['id','title','content','progress']   



class laravelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Laravel
        fields=['id','title','content','progress']                     



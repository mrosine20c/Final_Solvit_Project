from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from Stacks.models import DjangoModel,Node,React,Ui_ux,Laravel
from Stacks.serializers import DjangoSerializer, NodeSerializer, ReactSerializer, UiSerializer, laravelSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class DjangoModelViewset(ModelViewSet):
    queryset = DjangoModel.objects.all()
    serializer_class = DjangoSerializer
    


class NodeModelViewset(ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class ReactModelViewset(ModelViewSet):
    queryset = React.objects.all()
    serializer_class = ReactSerializer   


class UiModelViewset(ModelViewSet):
    queryset = Ui_ux.objects.all()
    serializer_class = UiSerializer  


class LaravelModelViewset(ModelViewSet):
    queryset = Laravel.objects.all()
    serializer_class = laravelSerializer        
        

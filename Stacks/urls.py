from Stacks import views
from django.db import router
from django.urls import path
from rest_framework import routers


router = routers.DefaultRouter()
router.register("django_stack", views.DjangoModelViewset,basename="django_stack")
router.register("node_stack", views.NodeModelViewset,basename="node_stack")
router.register("react_stack", views.ReactModelViewset,basename="react_stack")
router.register("ui_stack", views.UiModelViewset,basename="ui_stack")
router.register("laravel_stack", views.LaravelModelViewset,basename="laravel_stack")
urlpatterns = [
    
]+ router.urls
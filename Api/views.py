from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializer import (TestimonalSerializer,
                         AboutSerailizer,
                         WorkSerializer,
                         WorkExperianceSerializer,
                        SkillsSerializer,
                        BrandSerializer,
                        ContactSerializer)
from .models import Testimonal,About,Work,Experience,Skill,Brand
from django.middleware.csrf import get_token
# Create your views here.

@api_view(["GET"])
def Get_Token(request):
    token =get_token(request)
    return Response({"token":token})
@api_view(["Get"])
def home(request):
    data = TestimonalSerializer(Testimonal.objects.all(),many=True)
    return Response(data.data)
@api_view(["GET"])
def AboutFetch(request):
    data =AboutSerailizer(About.objects.all(),many=True)
    return Response(data.data)
@api_view(['GET'])
def WorkFetch(request):
    data = WorkSerializer(Work.objects.all(),many=True)
    return Response(data.data)


@api_view(['GET'])
def WorkExperienceFetch(request):
    data = WorkExperianceSerializer(Experience.objects.all(),many=True)
    return Response(data.data)

@api_view(['GET'])
def SkiilFetch(request):
    data = SkillsSerializer(Skill.objects.all(),many=True)
    return Response(data.data)

@api_view(['GET'])
def BrandFetch(request):
    data = BrandSerializer(Brand.objects.all(),many=True)
    return Response(data.data)


@api_view(['GET'])
def TestimonialFetch(request):
    data = BrandSerializer(Brand.objects.all(),many=True)
    return Response(data.data)

class PostContact(APIView):
    permission_classes = ()
    authentication_classes = ()
    def post(self, request, *args, **kwargs):
        serailizer =ContactSerializer(data=request.data)
        if(serailizer.is_valid()):
            serailizer.save()
            return Response(status=201)
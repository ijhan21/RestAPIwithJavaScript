from django.shortcuts import render
from rest_framework.views import APIView
from .models import SubCategory, Dataset
from .serializers import DatasetSerializer
from django.http import HttpResponse, JsonResponse


# Create your views here.
class Question(APIView):
    def get(self, request, subcategory):
        query_set = Dataset.objects.filter(subcategory=subcategory)
        serializer = DatasetSerializer(query_set, many=True)        
        return JsonResponse(serializer.data, safe=False)

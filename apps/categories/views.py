
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from .models import Categories
from .serializers import CategorySerializer
from rest_framework.response import Response

class CategoriesAPIView(APIView):
    def get(self, request):
        objetos = Categories.objects.all().order_by('-created_at')
        serializer = CategorySerializer(objetos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status
from myapp.models import Image
from .serializers import ImageSerializer

# Decorator-based views

@api_view(['GET'])
def api_image_list(request):
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_image_create(request):
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def api_image_detail(request, pk):
    image = generics.get_object_or_404(Image, pk=pk)
    if request.method == 'GET':
        serializer = ImageSerializer(image)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ImageSerializer(image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# ########################################################################

# class ImageListCreateView(APIView):
#     def get(self, request, format=None):
#         images = Image.objects.all()
#         serializer = ImageSerializer(images, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ImageDetailView(APIView):
#     def get_object(self, pk):
#         return generics.get_object_or_404(Image, pk=pk)

#     def get(self, request, pk, format=None):
#         image = self.get_object(pk)
#         serializer = ImageSerializer(image)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         image = self.get_object(pk)
#         serializer = ImageSerializer(image, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         image = self.get_object(pk)
#         image.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CategoryListCreateView(APIView):
#     def get(self, request, format=None):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CategoryDetailView(APIView):
#     def get_object(self, pk):
#         return generics.get_object_or_404(Category, pk=pk)

#     def get(self, request, pk, format=None):
#         category = self.get_object(pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         category = self.get_object(pk)
#         serializer = CategorySerializer(category, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         category = self.get_object(pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
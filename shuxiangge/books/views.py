from rest_framework import viewsets

from .serializers import Category, CategorySerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

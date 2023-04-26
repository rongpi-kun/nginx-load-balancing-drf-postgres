from django.shortcuts import render
from rest_framework.views import APIView
from . models import Books
from rest_framework.response import Response
from . serializers import BookSerializer

class ShowBooks(APIView):
    def get(self, request):
        my_model = Books.objects.all()
        print(my_model)
        serializer = BookSerializer(my_model, many=True)
        print(serializer)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        model = BookSerializer(data=data)
        if model.is_valid():
            model.save()
        return Response(model.data)
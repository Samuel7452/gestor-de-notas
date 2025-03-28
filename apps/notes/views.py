from .models import Notes
from .serializers import NotesSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.generics import UpdateAPIView

class NotesAPIView(APIView):
    def get(self, request):
        objetos = Notes.objects.all().order_by('-created_at')
        serializer = NotesSerializer(objetos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class NoteDeleteView(generics.DestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

class NotesUpdateView(UpdateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


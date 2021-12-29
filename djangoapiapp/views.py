from django.shortcuts import render
from rest_framework import viewsets
from .models import Apicursos
from .serializers import ApicursosSerializer

# Create your views here.

class ApiView(viewsets.ModelViewSet):
    queryset = Apicursos.objects.all()
    serializer_class = ApicursosSerializer

def home(request):
    return render(request, 'home.html', {})


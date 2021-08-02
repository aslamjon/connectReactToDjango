from django.shortcuts import render

from .models import Student
from rest_framework import viewsets
from .serializer import StudentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

def index(request):
    obj = Student.objects.all()
    context = {}
    if len(obj) == 0:
        context["obj"] = []
    else:
        context["obj"] = obj
    return render(request, 'index.html', context)

class StudentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    authentication_classes=(TokenAuthentication,)
    # permission_classes=(IsAuthenticated,)

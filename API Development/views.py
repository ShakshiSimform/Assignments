from rest_framework import generics, permissions, filters
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields= ['status']  
    ordering_fields = ['due_date']

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


    def get(self, request, *args, **kwargs):
        users = User.objects.all().values('username')
        return Response(users)



@csrf_exempt

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')  
        
        if username and password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({"message": "User registered successfully!"})
        else:
            return JsonResponse({"error": "Username and password are required."}, status=400)
    return JsonResponse({"error": "Invalid method"}, status=400)


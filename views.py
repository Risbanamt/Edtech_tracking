from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import User
from rest_framework import status
from rest_framework.permissions import AllowAny



#signup view

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    username = request.data.get('username')
    password = request.data.get('password')
    role = request.data.get('role')

    if not username or not password or not role:
        return Response({'error': 'Please provide username, password, and role'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)

    user = User.objects.create_user(username=username, password=password, role=role)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'message': 'User created successfully', 'token': token.key})


#login view

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    from django.contrib.auth import authenticate
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'role': user.role  
        })
    
    return Response({'error': 'Invalid credentials'}, status=400)



#Assignment creating view for Teachers

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_assignment(request):
    if request.user.is_staff:
        title = request.data.get('title')
        description = request.data.get('description')
        
        return Response({'message': 'Assignment created'})
    return Response({'error': 'Only teachers can create assignments'}, status=403)


#Assignment submitting View for students

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def submit_assignment(request):
    if not request.user.is_staff:
        assignment_id = request.data.get('assignment_id')
        content = request.data.get('content')
        
        return Response({'message': 'Submitted successfully'})
    return Response({'error': 'Only students can submit'}, status=403)



#Assignment listing views for Teachers
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def view_submissions(request):
    if request.user.is_staff:
        
        return Response({'submissions': []})  
    return Response({'error': 'Only teachers can view submissions'}, status=403)


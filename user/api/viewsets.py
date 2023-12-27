from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from user.models import (
    User,
    Teacher,
    Student,
    Admin,
    StudentSchoolYear
)
from school_year.models import SchoolYear
from user.api.serializers import (
    UserSerializer,
    StudentSerializer,
    TeacherSerializer,
    AdminSerializer,
    StudentSchoolYearSerializer
)
from user.permissions import UserPermission
from user.models import User, Student, Teacher
from user.api.serializers import UserSerializer


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [UserPermission]

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        queryset = User.objects.all()
        if user_id:
            queryset = queryset.filter(id=user_id)

        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        print(f'DATA::: {data}')
        hashed_password = make_password(data['password'])

        user = User.objects.create(
            email=data['email'],
            password=hashed_password,
            first_name=data['first_name'],
            last_name=data['last_name'],
            user_type=data['user_type']
        )
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
    @action(detail=False, methods=['PUT'])
    def update_student(self, request):
        email = request.data.get('email', None)
        
        if not email:
            return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User, email=email)
        
        if self.request.user.user_type != 'admin':
            return Response({'error': 'Você não tem autorização para realizar essa ação.'}, status=status.HTTP_403_FORBIDDEN)

        student = get_object_or_404(Student, user=user)
        print(student.user)
        serializer = StudentSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['PUT'])
    def update_teacher(self, request):
        email = request.data.get('email', None)
        if not email:
            return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = get_object_or_404(User, email=email)
        if self.request.user.user_type != 'admin':
            return Response({'error': 'Você não tem autorização para realizar essa ação.'}, status=status.HTTP_403_FORBIDDEN)
        
        teacher = get_object_or_404(Teacher, user=user)
        serializer = TeacherSerializer(teacher, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=False, methods=['PUT'])
    def update_admin(self, request):
        email = request.data.get('email', None)
        if not email:
            return Response({'error': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = get_object_or_404(User, email=email)
        if self.request.user.user_type != 'admin':
            return Response({'error': 'Você não tem autorização para realizar essa ação.'}, status=status.HTTP_403_FORBIDDEN)
        
        admin = get_object_or_404(Admin, user=user)
        serializer = AdminSerializer(admin, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    @action(detail=False, methods=['POST'])
    def student_year(self, request):
        if self.request.user.user_type != 'admin':
            return Response({'error': 'Você não tem autorização para realizar essa ação.'}, status=status.HTTP_403_FORBIDDEN)
        
        year = SchoolYear.objects.filter(
            year=request.data.get('year')
        ).first()
        student = Student.objects.filter(
            pk=request.data.get('student')
        ).first()
        
        user = StudentSchoolYear.objects.create(
            student=student,
            year=year
        )
        serializer = StudentSchoolYearSerializer(user)
        
        return Response(serializer.data)
    

class StudentViewset(ModelViewSet):
    serializer_class = StudentSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [UserPermission]

    def get_queryset(self):
        classes = self.request.query_params.get('classes', None)
        queryset = Student.objects.prefetch_related(
            'user'
        ).filter(user__user_type='student')
        
        return queryset

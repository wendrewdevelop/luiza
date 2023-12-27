from rest_framework import serializers
from user.models import (
    User,
    Student,
    Teacher,
    Admin,
    StudentSchoolYear
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'first_name', 
            'last_name', 
            'email', 
            'user_type',
            'password'
        )
        extra_kwargs = {'password': {'write_only': True}}


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    school_year_name = serializers.CharField(source='school_year.year', read_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"


class StudentSchoolYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSchoolYear
        fields = "__all__"
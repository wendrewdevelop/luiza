import json
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from report_card_grades.models import ReportCard
from report_card_grades.api.serializers import ReportCardSerializer
from user.permissions import UserPermission
from user.models import User, Student, Teacher


class ReportCardViewset(ModelViewSet):
    queryset = ReportCard.objects.all()
    serializer_class = ReportCardSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermission]

    def get_queryset(self):
        user_id = self.request.query_params.get('student_id', None)
        queryset = ReportCard.objects.all()
        if user_id:
            queryset = queryset.filter(student_id=user_id)

        return queryset
    
    def create(self, request, *args, **kwargs):
        data = request.data
        student_id = data.get('student')
        student = User.objects.filter(pk=student_id).first()

        if self.request.user.user_type == 'student':
            return Response({'error': 'Você não tem autorização para realizar essa ação.'}, status=status.HTTP_403_FORBIDDEN)

        report_card_instance = ReportCard.objects.create(
            student=student,
            grade=data['grade']
        )
        serializer = ReportCardSerializer(report_card_instance)
        return Response(serializer.data)
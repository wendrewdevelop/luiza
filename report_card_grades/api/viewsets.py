import json
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from report_card_grades.models import ReportCard
from report_card_grades.api.serializers import ReportCardSerializer
from user.permissions import UserPermission
from user.models import User
from rules.models import Rules
from school_subject.models import Subject


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
        grade_level = None

        if self.request.user.user_type == 'student':
            return Response({'error': 'Você não tem autorização para realizar essa ação.'}, status=status.HTTP_403_FORBIDDEN)
        
        grade_average_rule = Rules.objects.filter(
            rule_type='grade_average'
        ).first()

        subject_instance = Subject.objects.filter(
            pk=data['subject']
        ).first()

        if data['grade'] >= json.loads(grade_average_rule.rule_action):
            grade_level = '#0d9431'
        else:
            grade_level = '#f50000'
                
        report_card_instance = ReportCard.objects.create(
            student=student,
            grade=data['grade'],
            grade_level=grade_level,
            subject=subject_instance
        )
        serializer = ReportCardSerializer(report_card_instance)
        return Response(serializer.data)
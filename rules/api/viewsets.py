from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rules.models import Rules
from rules.api.serializers import RuleSerializer
from user.permissions import UserPermission


"""
    rule_list = [
        'grade_arrangement', # regra que define se as notas serão bimestrais, semestrais ou trimestrais.
        'grade_average', # regra que define a média escolar
        'students_by_class', # quantidade de alunos por sala,
        '': #,
    ]      

    arrangement_list = [
        'bi', # Bimestral.
        'sem', # Semestral
        'tri', # Trimestral
    ]    
"""

class RuleViewset(ModelViewSet):
    serializer_class = RuleSerializer
    # permission_classes = [UserPermission]

    def get_queryset(self):
        return Rules.objects.all()

    @action(detail=False, methods=['POST'])
    def basic_rules(self, request, *args, **kwargs):
        data = request.data
        rule_type = data.get('rule_type')
        rule_action = data.get('rule_action')
        arrangement = {f"{rule_type}": f"{rule_action}"}
        description = None

        match rule_type:
            case 'grade_arrangement':
                description = 'Regra criada para definir se as notas serão bimestrais, semestrais ou trimestrais.'
            case 'grade_average':
                description = 'Regra criada para definir a nota média.'

        instance = Rules.objects.create(
            rule_type=rule_type,
            rule_description=description,
            rule_action=arrangement
        )
        instance.save()
        
        return Response({'Message': 'Regra criada com sucesso!'})
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rules.models import Rules
from rules.api.serializers import RuleSerializer
from user.permissions import UserPermission
from luiza.pipeline import rules_pipeline


"""
    rule_list = [
        'grade_arrangement', # regra que define se as notas serão bimestrais, semestrais ou trimestrais.
        'grade_average', # regra que define a média escolar
        '', #
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
    def grade_arrangement(self, request, *args, **kwargs):
        data = request.data
        rule_type = data.get('rule_type')
        arrangement = {f"{rule_type}": f"{data.get('rule_action')}"}
        description = 'Regra criada para definir se as notas serão bimestrais, semestrais ou trimestrais.'

        instance = rules_pipeline[rule_type](arrangement, rule_type, description)
        
        return Response({'Message': instance})
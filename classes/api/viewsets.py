import random
from django.apps import apps
from django.db import models
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from classes.models import Video, Class
from classes.api.serializers import (
    VideoSerializer, 
    ClassSerializer
)
from user.permissions import UserPermission
from user.models import User, StudentSchoolYear, Student
from school_year.models import SchoolYear


class VideoViewset(ModelViewSet):
    serializer_class = VideoSerializer
    permission_classes = [UserPermission]

    def get_queryset(self):
        # if self.request.user
        return Video.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super(VideoViewset, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(VideoViewset, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(VideoViewset, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(VideoViewset, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(VideoViewset, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(VideoViewset, self).partial_update(request, *args, **kwargs)
    

class ClassViewset(ModelViewSet):
    serializer_class = ClassSerializer
    # permission_classes = [UserPermission]

    def create(self, request, *args, **kwargs):
        classes = Class()
        data = request.data

        student = Student.objects.get(pk=data['student'])
        print(f'STUDENT::: {student.pk}')
        school_year = SchoolYear.objects.get(pk=data['year'])
        print(f'YEAR::: {school_year.year}')
        student_year = StudentSchoolYear.objects.filter(
            year=school_year.pk,
            student=student.pk
        )
        print(f'STUDENT YEAR::: {student_year}')

        try:
            classes.create_dynamic_model_class_and_organize_students(
                school_year=school_year,
                student=student
            )

            return Response(
                {
                    'status': 'success', 
                    'message': 'Classe criada!'
                }
            )
        except Exception as error:
            return Response(
                {
                    'status': 'error', 
                    'message': f'{error}'
                }
            )
    
    def destroy(self, request, *args, **kwargs):
        data = request.data

        # Remove the reference to the dynamic model class
        del data['model_name']

        # Run Django migrations to delete the corresponding database table
        from django.core.management import call_command
        call_command('makemigrations', 'classes')
        call_command('migrate', 'classes')

        return Response({'status': 'success', 'message': 'Dynamic model deleted'})
    
    def list(self, request, *args, **kwargs):
        # Use Django apps module to get a list of all installed models
        all_models = apps.get_models()

        # Retrieve data for each model
        model_data = {}
        for model in all_models:
            model_name = model.__name__
            model_data[model_name] = self.get_model_data(model)

        return Response(model_data)

    def get_model_data(self, model):
        # Query the database to retrieve data for a given model
        model_data = []
        model_instances = model.objects.all()
        for instance in model_instances:
            model_data.append(self.serialize_instance(instance))
        return model_data

    def serialize_instance(self, instance):
        # Serialize a model instance to a dictionary
        return {
            field.name: getattr(instance, field.name)
            for field in instance._meta.fields
        }
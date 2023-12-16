from django.db import models, connection
from user.models import Student, User
from school_year.models import SchoolYear
from luiza.utils import generate_alphabet_series
from rules.models import Rules


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    school_year = models.ForeignKey(
        SchoolYear,
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        db_table = 'tb_video'


class Class:
    fields = {
        'student': models.CharField(
            max_length=150,
            null=False,
            blank=False
        ),
        'school_year': models.CharField(
            max_length=150,
            null=False,
            blank=False
        ),
        'serie': models.CharField(
            'Série escolar (A, B, C, ETC...)',
            max_length=30,
            null=False,
            blank=False
        )
    }

    def create_dynamic_model_class_and_organize_students(self, school_year, student):
        model_name = f'Class{school_year.year}'
        letter = None
        print(f'MODEL NAME::: {model_name}')
        STUDENTS_PER_CLASS = Rules.objects.filter(
            rule_type="students_by_class"
        ).first()

        # Create a new model class dynamically
        model = type(model_name, (models.Model,), {'__module__': 'classes', **self.fields})

        # Register the dynamic model with the database
        model._meta.app_label = 'classes'
        model._meta.db_table = f'tb_class_{school_year.year}'

        self.create_table_if_not_exists(model)

        students_queryset = User.objects.filter(
            user_type='student',
            student__school_year=school_year
        ).all()
        student_names = [student.first_name for student in students_queryset]
        # Generate an alphabet series
        alphabet_series = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        # Assign letters to students
        for i, student_name in enumerate(student_names, start=1):
            letter_index = (i - 1) // int(STUDENTS_PER_CLASS.rule_action)  # Calculate the index in the alphabet series
            letter = alphabet_series[letter_index]
            print(f"{student_name}: {letter}")

            # Now you can use dynamic model like any other Django model
            instance = model(
                school_year=school_year.year, 
                student=student_name,
                serie=letter
            )
            instance.save()

    def create_table_if_not_exists(self, model_class):
            # Check if the table exists in the database
            table_name = model_class._meta.db_table
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
                table_exists = cursor.fetchone() is not None

            # If the table does not exist, create it
            if not table_exists:
                with connection.schema_editor() as schema_editor:
                    schema_editor.create_model(model_class)


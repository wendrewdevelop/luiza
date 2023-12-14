import cv2
import numpy as np
from rules.models import Rules


def convert_frame_to_jpeg(frame):
    # Converte o frame para o formato JPEG
    _, buffer = cv2.imencode('.jpg', frame)
    
    # Converte o buffer para bytes
    frame_jpeg = buffer.tobytes()

    return frame_jpeg


def define_report_card_rule_grade_arrangement(
    arrangement: str, 
    rule_type: str, 
    description: str = None
):
    try:
        instance = Rules.objects.create(
            rule_type=rule_type,
            rule_description=description,
            rule_action=arrangement
        )

        instance.save()
        return 'Regra criada com sucesso!'
    except Exception as error:
        print(error)
        return error

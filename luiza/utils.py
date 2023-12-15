import cv2
import numpy as np


def convert_frame_to_jpeg(frame):
    # Converte o frame para o formato JPEG
    _, buffer = cv2.imencode('.jpg', frame)
    
    # Converte o buffer para bytes
    frame_jpeg = buffer.tobytes()

    return frame_jpeg

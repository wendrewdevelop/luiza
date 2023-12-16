import cv2
import numpy as np
import string


def convert_frame_to_jpeg(frame):
    # Converte o frame para o formato JPEG
    _, buffer = cv2.imencode('.jpg', frame)
    
    # Converte o buffer para bytes
    frame_jpeg = buffer.tobytes()

    return frame_jpeg


def generate_alphabet_series():
    alphabet = list(string.ascii_uppercase)
    series = []
    for i in range(26):
        series.extend(alphabet)
    return series

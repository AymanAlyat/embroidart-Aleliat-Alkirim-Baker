
from PIL import Image
import numpy as np
import cv2
import os


class ImageProcessor:
    pass

def load_image(self, path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image file not found: {path}")

    return Image.open(path).convert("RGB")


def to_numpy(self, image):
    return np.array(image)
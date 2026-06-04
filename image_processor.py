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


def resize_for_embroidery(self, image):
    image.thumbnail((150, 150), Image.LANCZOS)
    return image


def detect_edges(self, image):
    image_array = np.array(image)

    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)

    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    edges = cv2.Canny(blurred, 50, 150)

    return edges
from PIL import Image, ImageDraw


def create_test_image(output_path="test_flower.png"):
   img = Image.new("RGB", (200, 200), (255, 255, 255))
   draw = ImageDraw.Draw(img)
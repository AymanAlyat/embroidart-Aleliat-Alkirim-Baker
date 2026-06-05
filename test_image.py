from PIL import Image, ImageDraw


def create_test_image(output_path="test_flower.png"):
   img = Image.new("RGB", (200, 200), (255, 255, 255))
   draw = ImageDraw.Draw(img)

   draw.ellipse([80, 80, 120, 120], fill=(255, 215, 0))

petals = [
    (60, 90), (140, 90), (90, 60), (90, 140),
    (65, 65), (135, 65), (65, 135), (135, 135)
]

for x, y in petals:
    draw.ellipse([x-15, y-15, x+15, y+15], fill=(255, 100, 150))

draw.ellipse([10, 10, 60, 60], fill=(100, 200, 100))
draw.line([35, 60, 35, 190], fill=(34, 139, 34), width=4)
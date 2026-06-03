import argparse
from image_processor import ImageProcessor


from pattern_generator import PatternGenerator
from visualizer import Visualizer

from file_manager import FileManager



def cmd_generate(args):

    processor = ImageProcessor()#instance

    generator = PatternGenerator()
    visualizer = Visualizer()
    manager = FileManager()
    image = processor.load_image(args.image)

    image = processor.resize_for_embroidery(image)

    edge_map = processor.detect_edges(image)

    index_map, colors = processor.quantize_colors(image,args.colors)


    stitches = generator.generate_pattern(edge_map,index_map,colors)


def cmd_preview(args):
    pass
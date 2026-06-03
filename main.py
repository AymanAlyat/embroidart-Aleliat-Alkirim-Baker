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

    if args.output:#if the val ==>then give true

        if args.output.endswith(".json"):
            manager.save_json(stitches, args.output)

        elif args.output.endswith(".csv"):
            manager.save_csv(stitches, args.output)

#Embrodary task 2.3



    if not args.no_preview:

        if args.compare:


            visualizer.compare_original_and_pattern(image,stitches)

        else:
            visualizer.preview_pattern(stitches)


def cmd_preview(args):
    pass
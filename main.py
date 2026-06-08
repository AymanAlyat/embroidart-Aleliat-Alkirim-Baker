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


    visualizer.show_thread_colors(colors)


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


    manager = FileManager()
    visualizer = Visualizer()

    #you should know the type extention

    if args.file.endswith(".json"):
        stitches = manager.load_json(args.file)

    elif args.file.endswith(".csv"):
        stitches = manager.load_csv(args.file)



    visualizer.preview_pattern(stitches)


def main():#from your template in git hup

    parser = argparse.ArgumentParser(description="EmbroidArt CLI — Smart Mini Embroidery Pattern Generator")

    subparsers = parser.add_subparsers(dest="command", required=True)


    gen = subparsers.add_parser( "generate", help="Generate pattern from an image")


    gen.add_argument("image")

    gen.add_argument("--colors", type=int, default=6)



    gen.add_argument("--output","-o")

    gen.add_argument( "--compare", action="store_true")


    gen.add_argument( "--no-preview", action="store_true")

    gen.set_defaults(func=cmd_generate)

    prev = subparsers.add_parser( "preview",help="Preview a saved pattern file")



    prev.add_argument("file")

    prev.set_defaults(func=cmd_preview)


    args = parser.parse_args()
    args.func(args)






if __name__ == "__main__":
    main()
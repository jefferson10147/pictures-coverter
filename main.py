import argparse
from ast import parse
import os
from PIL import Image


def convert_from_jpg_to_png(jpg_file, output_file):
    img = Image.open(jpg_file)
    img.convert("RGB").save(output_file, "PNG")


def compress_file(input_file, output_file, input_folder, output_folder, quality):
    img = Image.open(input_folder + input_file)
    img.convert("RGB").save(
        output_folder + output_file, "JPEG", quality=int(quality))


def compress_all_files(path, extension=".jpg", save_path="./", quality=30):
    for file in os.listdir(path):
        if file.endswith(extension):
            compress_file(file, save_path, quality)


def cli():
    parser = argparse.ArgumentParser(description="Convert image to jpg")
    parser.add_argument("-i", "--input", help="Input image", required=True)
    parser.add_argument("-o", "--output", help="Output image", required=True)
    parser.add_argument("--input_folder", help="Input folder", required=False, default="./")
    parser.add_argument("--output_folder", help="Output folder", required=False, default="./")
    parser.add_argument("-q", "--quality", help="Quality of output image", required=False, default=30)
    
    # parser.add_argument("-a", "--all", help="Compress all files in directory", action="store_true")
    # parser.add_argument("-e", "--extension", help="Extension of files to compress", default=".jpg")

    return parser.parse_args()


def main():
    args = cli()

    # if args.all:
    #    compress_all_files(args.input, args.extension, args.output, args.quality)
    # elif args.cjpg:
    #    convert_from_jpg_to_png(args.input, args.output)
    # else:
    
    compress_file(args.input, args.output, args.input_folder, args.output_folder, args.quality)
    
    
if __name__ == "__main__":
    main()

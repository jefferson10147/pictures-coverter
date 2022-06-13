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


def convert_all_files(input_folder, output_folder, extension, final_extension, quality):
    for file in os.listdir(input_folder):
        if file.endswith(extension):
            print("Compressing file: " + file)
            compress_file(file, file.replace(extension, final_extension), input_folder, output_folder, quality)


def cli():
    parser = argparse.ArgumentParser(description="Convert image to jpg")
    parser.add_argument("-i", "--input", help="Input image", required=False)
    parser.add_argument("-o", "--output", help="Output image", required=False)
    parser.add_argument("--input_folder", help="Input folder", required=False, default="./")
    parser.add_argument("--output_folder", help="Output folder", required=False, default="./")
    parser.add_argument("-q", "--quality", help="Quality of output image", required=False, default=30)
    parser.add_argument("-a", "--all", help="Compress all files in directory", action="store_true")
    parser.add_argument("-e", "--extension", help="Extension of files to compress", default=".jpg")
    parser.add_argument("--final_extension", help="Extension of files to compress", default=".png")

    return parser.parse_args()


def main():
    args = cli()

    if args.all:
        convert_all_files(
            args.input_folder, args.output_folder, args.extension, args.final_extension, args.quality)
    else:
        compress_file(args.input, args.output, args.input_folder, args.output_folder, args.quality)
    
    
if __name__ == "__main__":
    main()

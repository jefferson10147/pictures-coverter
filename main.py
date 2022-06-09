import argparse
from ast import parse
import os
from PIL import Image


def compress_file(file, save_path="./", quality=30):
    img = Image.open(file)
    img.convert("RGB").save(save_path, "JPEG", quality=int(quality))


def compress_all_files(path, extension, save_path, quality):
    for file in os.listdir(path):
        if file.endswith(extension):
            compress_file(file, save_path, quality)


def cli():
    parser = argparse.ArgumentParser(description="Convert image to jpg")
    parser.add_argument("-i", "--input", help="Input image", required=True)
    parser.add_argument("-o", "--output", help="Output image", required=True)
    parser.add_argument("-q", "--quality", help="Quality of output image", required=True)
    parser.add_argument("-a", "--all", help="Compress all files in directory", action="store_true")

    return parser.parse_args()


def run():
    args = cli()

    img = Image.open(args.input)
    img.convert("RGB").save(args.output, "JPEG", quality=int(args.quality))

    #with Image.open("test.jpg") as img:
    #    img.convert("RGB").save("test_picture.jpg", quality=30)


if __name__ == "__main__":
    run()

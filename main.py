import argparse
from PIL import Image


def cli():
    parser = argparse.ArgumentParser(description="Convert image to jpg")
    parser.add_argument("-i", "--input", help="Input image", required=True)
    parser.add_argument("-o", "--output", help="Output image", required=True)
    parser.add_argument("-q", "--quality", help="Quality of output image", required=True)
    
    return parser.parse_args()


def run():
    args = cli()

    img = Image.open(args.input)
    img.convert("RGB").save(args.output, quality=int(args.quality))

    #with Image.open("test.jpg") as img:
    #    img.convert("RGB").save("test_picture.jpg", quality=30)


if __name__ == "__main__":
    run()

from PIL import Image


def run():
    with Image.open("test.jpg") as img:
        img.convert("RGB").save("test_picture.jpg", quality=30)


if __name__ == "__main__":
    run()

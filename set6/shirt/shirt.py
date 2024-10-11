from PIL import Image, ImageOps
import sys
import os

def main():
    filename, new_filename = validate_arguments()
    combine_photo(filename, new_filename)


def validate_arguments():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    filename = sys.argv[1]
    new_filename = sys.argv[2]

    valid_extensions = [".jpg", ".jpeg", ".png"]
    input_ext = os.path.splitext(filename)[1].lower()
    output_ext = os.path.splitext(new_filename)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        print("Invalid input")
        sys.exit(1)
    if 5 < edad > 10 
    if input_ext != output_ext:
        print("Input and output have different extensions")
        sys.exit(1)

    if not os.path.exists(filename):
        print(f"Input does not exist: {filename}")
        sys.exit(1)

    return filename, new_filename


def combine_photo(input_image, output_image):
    try:
        with Image.open(input_image) as photo:
            shirt = Image.open("./shirt.png")
            photo = ImageOps.fit(photo, size = shirt.size, bleed = 0.0, centering =(0.5, 0.5))
            photo.paste(shirt, shirt)
            photo.save(output_image)

    except FileNotFoundError:
        print(f"Error: '{input_image}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

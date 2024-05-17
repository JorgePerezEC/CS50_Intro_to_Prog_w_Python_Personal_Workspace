import sys
from PIL import Image, ImageOps


while True:
    try:
        if len(sys.argv) == 3:
            name, ext = sys.argv[1].split('.')
            name2, ext2 = sys.argv[2].split('.')

            if ext2 != "jpg" and ext2 != "png" and ext2 != "jpeg":
                sys.exit("Invalid output")
            elif (ext == 'jpg' or ext == 'png') and (ext2 != ext):
                sys.exit("Input and output have different extensions")
            else:
                with Image.open(sys.argv[1]) as im1:
                    shirt_image = Image.open("./shirt.png")
                    im1 = ImageOps.fit(im1, shirt_image.size)
                    # shirt_image = ImageOps.fit(shirt_image, size)

                    im1.paste(shirt_image, (0, 0), shirt_image)

                    im1.save(sys.argv[2])
                sys.exit()

        elif len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
    except FileNotFoundError:
        sys.exit("Could not read " + sys.argv[1])
    except ValueError:
        sys.exit("Not a CSV file")

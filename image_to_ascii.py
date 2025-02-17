from PIL import Image
import os
# To convert an image change the reference to the image right at the bottom of the file.


# image_to_ascii method converts an image to ascii characters.
def image_to_ascii(image, scale=2):
    # The method is executed if the file exists
    if os.path.exists(image) & image.endswith(".jpg"):
        # Opens the image.
        image = Image.open(image)

        # Calculates the dimensions of the image.
        width, height = image.size

        # Converts the image to grayscale.
        image = image.convert("L")

        # Makes an empty text document or emptys the already existing one.
        ascii_image = open("ascii_image.txt", "w")
        ascii_image.close()
        ascii_image = open("ascii_image.txt", "a")

        # Goes through each pixel.
        for y in range(height):

            for x in range(width):

                # Determines the brightness of the pixel.
                brightness = image.getpixel((x, y))

                # Determines the symbol based on what the brightness of the symbol is.
                if brightness > 225:
                    symbol = "#"

                elif brightness > 193:
                    symbol = "X"

                elif brightness > 161:
                    symbol = "%"

                elif brightness > 129:
                    symbol = "&"

                elif brightness > 97:
                    symbol = "*"

                elif brightness > 65:
                    symbol = "+"

                elif brightness > 33:
                    symbol = "/"

                elif brightness > 0:
                    symbol = "'"

                else:
                    symbol = " "

                # Adds the symbol to the text document.
                ascii_image.write(symbol * scale)

            # Goes to the next line.
            ascii_image.write("\n")

        # Closes both files.
        image.close()
        ascii_image.close()


# This is the only line you need to edit, to change images. The scale of 2 seems to work fine.
image_to_ascii("change_me.jpg", 2)

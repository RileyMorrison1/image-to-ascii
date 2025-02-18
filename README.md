# image-to-ascii
Converts an image into ascii characters stored in a text document.

# Python Modules Used
- pillow
- os

# How To Use
To convert an image to ascii, the only line that needs to be changed is the last. Replace the "change_me.jpg" with the reference to the image that you want to use. When you run the code a new text file will be created with the ascii image within it, named "ascii_image.txt". If the text file has been created previously it will write over it, replacing the last ascii image with the new one. The file will be saved to the current working directory.

# Limitations
- The only picture format that can be converted currently are JPEGs. This is because the program checks if the image is real and does not convert it if the image is not found or a JPEG. This could be fixed by adding all picture formats to the validation check.
- If a text editor is used that is not using a font that makes the characters the same width, the ascii image will appear distorted.
- It is hard to view the ascii image if the image is large. This is because each pixel is represented in the ascii image making it too large to view. A fix to this would be to resize the image to a size that is manageable
 
# Preview
Ascii image of Albert Einstein

![code](https://github.com/user-attachments/assets/ecac4447-ef1d-462f-a8a3-8133e295f02c)

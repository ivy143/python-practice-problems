#program to find the size resolution of an image using PIL (Python Imaging Library)
from PIL import Image

# Open an image file
image_path = "path_to_your_image.jpg"  # Replace with the actual image path
image = Image.open(image_path)

# Get the size (resolution) of the image
width, height = image.size

print(f"Image resolution: {width}x{height}")
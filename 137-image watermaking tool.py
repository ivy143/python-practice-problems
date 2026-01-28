# Image Watermarking Tool
from PIL import Image, ImageDraw, ImageFont
import os
def add_watermark(input_image_path, output_image_path, watermark_text, position=(0, 0), opacity=128):
    base_image = Image.open(input_image_path).convert("RGBA")
    watermark = Image.new("RGBA", base_image.size)
    draw = ImageDraw.Draw(watermark)

    font_size = int(min(base_image.size) / 15)
    font = ImageFont.truetype("arial.ttf", font_size)

    text_width, text_height = draw.textsize(watermark_text, font)
    x, y = position
    if x < 0:
        x = base_image.width - text_width + x
    if y < 0:
        y = base_image.height - text_height + y

    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, opacity))

    watermarked_image = Image.alpha_composite(base_image, watermark)
    watermarked_image.convert("RGB").save(output_image_path, "JPEG")
# Example usage
input_image = "input.jpg"  # Path to your input image
output_image = "output.jpg"  # Path to save the watermarked image
watermark_text = "Sample Watermark"

add_watermark(input_image, output_image, watermark_text, position=(-10, -10), opacity=128)
print(f"Watermarked image saved as: {output_image}")
# This code adds a semi-transparent text watermark to an image using the Pillow library.
# Make sure to have the required library installed:
# pip install Pillow
# Note: You may need to adjust the font path in the ImageFont.truetype() function depending on your system.
# You can customize the input image path, output image path, watermark text, position, and opacity as needed for your specific use case.
# Ensure that the input image file exists in the specified path before running the script.

# QR Code Generator
import qrcode
def generate_qr_code(data, filename):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)
# Example usage
data = "https://www.example.com"
filename = "example_qr.png"
generate_qr_code(data, filename)
print(f"QR code generated and saved as: {filename}")
# This code generates a QR code for the provided data and saves it as an image file.
# Make sure to have the required library installed:
# pip install qrcode[pil]
# Note: You can customize the 'data' and 'filename' variables to generate QR codes for different information and save them with different names.
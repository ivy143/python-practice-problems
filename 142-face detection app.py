# Face Detection App
import cv2
def detect_faces(image_path, cascade_path='haarcascade_frontalface_default.xml'):
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cascade_path)

    # Read the input image
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the output image with detected faces
    cv2.imshow('Detected Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# Example usage
image_path = 'input.jpg'  # Path to your input image
detect_faces(image_path)
# This code detects faces in an image using OpenCV's Haar Cascade classifier and displays the image with rectangles drawn around detected faces.
# Make sure to have the required library installed:
# You can install OpenCV using pip:
# pip install opencv-python

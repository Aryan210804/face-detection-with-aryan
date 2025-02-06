import cv2
from google.colab.patches import cv2_imshow # Import cv2_imshow
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
def detect_faces(image_path):
    image = cv2.imread(image_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2_imshow(image) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    image_path = '/content/ak.jpg' 
    detect_faces('/content/ak.jpg')
    if __name__ == "__main__":
      image_path = '/content/a.jpg'
      detect_faces('/content/a.jpg')
      if __name__ == "__main__":
        image_path = '/content/WhatsApp Image 2025-02-06 at 6.51.10 PM.jpeg' 
        detect_faces('/content/WhatsApp Image 2025-02-06 at 6.51.10 PM.jpeg')

import cv2
import dlib
import os
import boto3

# Initialize Rekognition client
rekognition_client = boto3.client('rekognition')

# Initialize Rekognition client
rekognition_client = boto3.client('rekognition')

# Function to recognize celebrities using *****Amazon Rekognition*****
def recognize_celebrities(image_path):
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    try:
        # Call Rekognition to recognize celebrities
        response = rekognition_client.recognize_celebrities(
            Image={'Bytes': image_bytes}
        )
        confidence = response.get("Confidence") 
        celebrities = response.get('CelebrityFaces', [])
        
        if celebrities:
            print("Celebrities recognized:")
            for celeb in celebrities:
                #print(celeb)
                name = celeb.get('Name', 'Unknown')
                confidence = celeb.get('MatchConfidence', 'N/A')
                print(f"Name: {name}, Confidence: {confidence}")
        else:
            print("No celebrities detected.")
    
    except Exception as e:
        print(f"Error recognizing celebrities: {e}")


# Function for detecting handshakes (simple placeholder using face detection)
def detect_handshake(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()
    faces = detector(gray)
    
    # Simple placeholder logic for handshake detection (two faces in an image)
    if len(faces) > 1:
        return True
    return False
    #limitation to this code is that it assumes that if atleast two faces exist in the image
    #then a handshake is detected.


# Initialize *******Google Vision API******* client
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/mahdimetwally/Downloads/integral-cat-444116-b5-942100a6bef8.json"
##from google.cloud import vision
#client = vision.ImageAnnotatorClient()


#will use google vision API to analyze images
#def analyze_image_with_Gvision(image_path):
    # Read the image file
   # with open(image_path, "rb") as image_file:
   #     content = image_file.read()
    
    # Create an image object for Vision API
   # image = vision.Image(content=content)
    
    # Call the API for label detection
   # response = client.face_detection(image=image)
  #  faces = response.face_annotations

    #response = client.label_detection(image=image)
    #labels = response.label_annotations
    
    # Print out labels detected in the image
   # likelihood_name = (
   #     "UNKNOWN",
    #    "VERY_UNLIKELY",
    #    "UNLIKELY",
    #    "POSSIBLE",
    #    "LIKELY",
    #    "VERY_LIKELY",
   # )
   # print("Faces:")

    #for face in faces:
     #   print(f"anger: {likelihood_name[face.anger_likelihood]}")
     #   print(f"joy: {likelihood_name[face.joy_likelihood]}")
     #   print(f"surprise: {likelihood_name[face.surprise_likelihood]}")
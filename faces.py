from PIL import Image
import face_recognition
from os import walk

def encode(image):
    return face_recognition.face_encodings(face_recognition.load_image_file(image))[0]

def loadKnownFaces():
    filenames = next(walk("faces"), (None, None, []))[2]  # [] if no file
    res = {}
    for filename in filenames:
        res[filename] = encode("faces/" + filename)
    return res

def getFacesFromImage(image):
    return face_recognition.face_encodings(face_recognition.load_image_file(image))
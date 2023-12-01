import face_recognition
import faces
import numpy as np

unknowns_faces = faces.getFacesFromImage("camera/biden-trump.jpg")

knowns = faces.loadKnownFaces()

a = 1
for unknown_face in unknowns_faces:
    vals = []
    keys = []
    for val in knowns.values():
        vals.append(val)
    for key in knowns.keys():
        keys.append(key)
    face_distances = face_recognition.face_distance(vals, unknown_face)
    
    i = 0
    for face_distance in face_distances:
        if face_distance < 0.5:
            print(keys[i] + ' matches on face #' + str(a))
        i += 1
    a += 1
        
print('All faces has been analyzed')
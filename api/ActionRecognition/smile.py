import os
from cv2 import cv2
from face_recognition import face_landmarks,face_locations

class Smile():
    def __init__(self):
        self.smileModelPath= os.path.join(os.path.dirname(__file__),
                             'utils/haarcascade_smile.xml') 
        self.smileModel = cv2.CascadeClassifier(self.smileModelPath)
        self.scaleFactor = 1.8
        self.minNeighbors = 12

    def _detect_face(self,image):
        print(image.shape)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # detect faces
        faces = face_locations(gray,0)
        if len(faces) == 0 or len(faces)>1:
            return False
        face = faces[0]
        top, right, bottom, left = face[0:4]
        # crop the face from the image
        cropped_gray = gray[top:bottom, left:right] 
        return cropped_gray

    def _smile_detector(self,face):
        print(face.shape)
        smiles = self.smileModel.detectMultiScale(face,self.scaleFactor, self.minNeighbors)
        if len(smiles) > 0 :
            return True
        else :
            return False

    def detector(self,image):

        face = self._detect_face(image)
        if face is False:
            return False
        smile = self._smile_detector(face)
        return smile
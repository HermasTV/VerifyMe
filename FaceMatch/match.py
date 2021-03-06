import face_recognition
from cv2 import cv2

class Matcher():
    def __init__(self):
        pass

    def _get_imgs(self,id_card,selfie):

        id_img = cv2.cvtColor(id_card,cv2.COLOR_BGR2RGB)
        selfie_img = cv2.cvtColor(selfie,cv2.COLOR_BGR2RGB)

        return id_img,selfie_img

    def match(self,id_card,selfie):
        id,selfie = self._get_imgs(id_card,selfie)
        #encode images
        id_encoding = face_recognition.face_encodings(id)[0]
        selfie_encoding = face_recognition.face_encodings(selfie)[0]
        #compair encodings
        result = face_recognition.compare_faces([id_encoding], selfie_encoding)
        return result
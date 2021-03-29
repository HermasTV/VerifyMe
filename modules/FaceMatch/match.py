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
        id_encoding = face_recognition.face_encodings(id)
        selfie_encoding = face_recognition.face_encodings(selfie)

        if len(selfie_encoding) ==0 or len(id_encoding) == 0 :
            raise ValueError(222)
        elif len(selfie_encoding) >1 or len(id_encoding)>1 :
            raise ValueError(223)
        else : 
            id_encoding = id_encoding[0]
            selfie_encoding = selfie_encoding[0]
        #compair encodings
        result = face_recognition.compare_faces([id_encoding], selfie_encoding)[0]
        
        if result == False :
            raise ValueError(221)

        return result

# if __name__ == "__main__":

#     idPath = '/media/hermas/Volume/Learing/UOL/Level5p2/agile/VerifyMe/testing/files/id.jpg'
#     selfiePath = '/media/hermas/Volume/Learing/UOL/Level5p2/agile/VerifyMe/testing/files/selfie.jpg'
#     idImg = cv2.imread(idPath)
#     selfieImg = cv2.imread(selfiePath)
#     match= Matcher()
#     res = match.match(idImg,selfieImg)

#     print(res)
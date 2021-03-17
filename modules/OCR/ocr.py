from cv2 import cv2
from PIL import Image
import easyocr
from .preprocessing import PreProcess
from traceback import print_exc
class OCR :

    def __init__(self):
        self.reader = easyocr.Reader(['ar'],gpu=False)
        self.processor = PreProcess()
        self.output = {}
    def recognize(self,data):
        try:

            cropped = self.processor.crop_id(data)
            fields = self.processor.extract(cropped)
            for key,value in fields.items():
                result = self.reader.readtext(value,detail=0,
                            contrast_ths=0.4,
                            paragraph=True,mag_ratio=1.5,
                            text_threshold=0.5)
                #results.reverse()
                #text = ' '.join(results)
                self.output[key] = result[0]

            return self.output
        except Exception as e :
            print_exc()
        
        

# if __name__ == "__main__":

#     ImgPath = 'utils/test2.jpg'
#     testImg = cv2.imread(ImgPath)
#     ocr= OCR()
#     fields = ocr.recognize(testImg)

#     for field in fields.values():
#             results = reader.readtext(field,detail=0)
#             for result in results:
#                 print(result)
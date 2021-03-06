from cv2 import cv2
import numpy as np
from PIL import Image
import os
#for arabic encoding
# -*- coding: utf-8 -*-

class PreProcess :

    def __init__(self):
        self.template = os.path.join(os.path.dirname(__file__),'utils/front.jpg')

    def crop_id(self,img):
        img1 = cv2.imread(self.template,cv2.IMREAD_GRAYSCALE)
        img2 = img.copy()
        # Initiate SIFT detector
        orb = cv2.SIFT_create()
        # find the keypoints and descriptors with ORB
        kp1, des1 = orb.detectAndCompute(img1,None)
        kp2, des2 = orb.detectAndCompute(img2,None)
        # create BFMatcher object
        bf = cv2.BFMatcher()
        # Match descriptors.
        matches = bf.knnMatch(des1,des2,k=2)

        good = []
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append(m)

        if len(good)>8:
            src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
            dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

            M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
            matchesMask = mask.ravel().tolist()
            print(img1.shape)
            h,w = img1.shape
            pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
            dst = cv2.perspectiveTransform(pts,M)

        else:
            print("Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT) )
            matchesMask = None

        width,height = 603,371
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        idx = [0,3,1,2]
        dst=dst[idx]
        M = cv2.getPerspectiveTransform(dst,pts2)
        res = cv2.warpPerspective(img2,M,(width,height))
        cv2.imwrite('logs/cropped.jpg',res)
        return res 

    def extract(self,front):
        """
        @Input  : image, (part := integer)
        @Output : contours of position

        @Intent : 
        crops the image using the defined algorithm for the document type

        @Assumptions (The less assumptions, the less coupling in the code) : 
        - right data format, no checking
        - no null stuff inserted
        """
        # Real Card width and height
        w = 8.6
        h = 5.5

        # init. card area parameters
        scaled_h = int(front.shape[0] *h )
        scaled_w = int(front.shape[1] *w )

        card_f = front
        card_f = cv2.resize(card_f, (scaled_w, scaled_h))

        face = card_f[int(0.06 * card_f.shape[0]): int(0.5 * card_f.shape[0]),
                    int(0.03 * card_f.shape[1]): int(0.27 * card_f.shape[1])]

        first_name = card_f[int(0.26 * card_f.shape[0]): int(0.36 * card_f.shape[0]),
                    int(0.6 * card_f.shape[1]): card_f.shape[1] - 10]

        last_name = card_f[int(0.355 * card_f.shape[0]): int(0.46 * card_f.shape[0]),
                        int(0.35 * card_f.shape[1]): card_f.shape[1] - 10]

        address_line1 = card_f[int(0.455 * card_f.shape[0]): int(0.57 * card_f.shape[0]),
                        int(0.32 * card_f.shape[1]): card_f.shape[1] - 10]

        address_line2 = card_f[int(0.57 * card_f.shape[0]): int(0.67 * card_f.shape[0]),
                        int(0.37 * card_f.shape[1]): card_f.shape[1] - 10]

        id_num = card_f[int(0.76 * card_f.shape[0]): int(0.9 * card_f.shape[0]),
                        int(0.42 * card_f.shape[1]): card_f.shape[1] - 10]

        serial = card_f[int(0.9 * card_f.shape[0]): card_f.shape[0] - 10,
                        int(0.05 * card_f.shape[1]): int(0.4 *card_f.shape[1] - 10)]

        # cv2.imwrite('logs/face.jpg',face)
        # cv2.imwrite('logs/first_name.jpg',first_name)
        # cv2.imwrite('logs/last_name.jpg',last_name)
        # cv2.imwrite('logs/address_line1.jpg',address_line1)
        # cv2.imwrite('logs/address_line2.jpg',address_line2)
        # cv2.imwrite('logs/id_num.jpg',id_num)
        # cv2.imwrite('logs/serial.jpg',serial)

        return dict(name = first_name,
                    family_name = last_name,
                    address_line_one = address_line1,
                    address_line_two = address_line2
                    )
 

if __name__ == "__main__":
    import easyocr

    reader = easyocr.Reader(['ar'],gpu=False,)
    imagePath = 'utils/test2.jpg'
    extractor = PreProcess()
    cropped = extractor.crop_id(imagePath)
    fields = extractor.extract(cropped)
    for field in fields.values():
        results = reader.readtext(field,detail=0)
        for result in results:
            print(result)
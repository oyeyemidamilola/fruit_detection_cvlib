
# import dependencies
import os

import cv2 as cv
import cvlib
import matplotlib.pyplot as plt
from cvlib.object_detection import draw_bbox

EXTENSIONS = {'png','jpeg','jpg','gif'}

def is_image(file):
    ''' checks if file is an image '''

    if os.path.splitext(file)[1].replace('.','').lower() in EXTENSIONS:
        return True
    raise Exception('File is not an image')

if __name__ == "__main__":

    ''' object detection '''
    
    try:
        image_dir = os.path.join(os.getcwd(),'images')
        for file in os.listdir(image_dir):
            file = os.path.join(image_dir,file)
            if is_image(file):
                image = cv.imread(file)
                boundaries , labels, confidence = cvlib.detect_common_objects(image)
                output = draw_bbox(image, boundaries, labels, confidence)
                plt.imshow(output)
                plt.show()
    except Exception as e:
        print(e)




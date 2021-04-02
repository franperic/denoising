import glob
import cv2 as cv

def load_images(paths):
    image_files = []

    for f in paths:
        image_files.append(sorted(glob.glob(f + "/*")))

    images = []
    for ff in image_files:
        curr = []
        for f in ff:
            curr.append(cv.imread(f, cv.IMREAD_GRAYSCALE))
        images.append(curr)
    
    return images
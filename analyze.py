from PIL import Image
import numpy as np
import time 
import math

print("====================================================")
startTime = time.time()
# filenames = ["LI_1_1000X.tif", "PMA_2_L.tif", "P_3_s.tif", "LI_1_L.tif", "PMA_2_s.tif", "LI_1_s.tif", "PMA_3_1000X.tif", "T4_1_1000X.tif", "LI_2_1000X.tif", "PMA_3_1000X2.tif", "T4_1_L.tif", "LI_2_L.tif", "PMA_3_L.tif", "T4_1_s.tif", "LI_2_s.tif", "PMA_3_s.tif", "T4_2_1000X.tif", "LI_3_1000X.tif", "P_1_1000X.tif", "T4_2_L.tif", "LI_3_L.tif", "P_1_L.tif", "T4_2_s.tif", "LI_3_s.tif", "P_1_s.tif", "T4_3_1000X.tif", "PMA_1_1000X.tif", "P_2_1000X.tif", "T4_3_L.tif", "PMA_1_L.tif", "P_2_L.tif", "T4_3_s.tif", "PMA_1_s.tif", "P_2_s.tif", "PMA_2_1000X.tif", "P_3_1000X.tif", "PMA_2_1000X2.tif", "P_3_L.tif"]
filenames_all = ['LI_1_1000X.tif', 'LI_1_L.tif', 'LI_1_s.tif', 'LI_2_1000X.tif', 'LI_2_L.tif', 'LI_2_s.tif', 'LI_3_1000X.tif', 'LI_3_L.tif', 'LI_3_s.tif', 'PMA_1_1000X.tif', 'PMA_1_L.tif', 'PMA_1_s.tif', 'PMA_2_1000X.tif', 'PMA_2_L.tif', 'PMA_2_s.tif', 'PMA_3_1000X.tif', 'PMA_3_L.tif', 'PMA_3_s.tif', 'P_1_1000X.tif', 'P_1_L.tif', 'P_1_s.tif', 'P_2_1000X.tif', 'P_2_L.tif', 'P_2_s.tif', 'P_3_1000X.tif', 'P_3_L.tif', 'P_3_s.tif', 'T4_1_1000X.tif', 'T4_1_L.tif', 'T4_1_s.tif', 'T4_2_1000X.tif', 'T4_2_L.tif', 'T4_2_s.tif', 'T4_3_1000X.tif', 'T4_3_L.tif', 'T4_3_s.tif']
filenames_1000X = []
filenames_L = []
filenames_s = []
for i in range(0, len(filenames_all)):
    if i % 3 == 0:
        filenames_1000X.append(filenames_all[i])
    if i % 3 == 1:
        filenames_L.append(filenames_all[i])
    if i % 3 == 2:
        filenames_s.append(filenames_all[i])

# 'PMA_2_1000X2.tif',  'PMA_3_1000X2.tif',

def getGreenIntensity(im, cutoff = True, cutoffIntensity = 500, maxIntensity = 5000, showImage = False):
    im.seek(0)
    imarray = np.array(im).astype(np.int64)     #np.int64 is the fastest, probably some weird optimization numpy did
    if cutoff:
        # imarray = np.array(list(map(lambda x: list(map(lambda y: 0 if y < cutoffIntensity else y, x)), imarray)))
        # imarray = np.array(list(map(lambda x: list(map(lambda y: 0 if y < cutoffIntensity else min(maxIntensity, y), x)), imarray)))
        # imarray = np.array(list(map(lambda x: list(map(lambda y: 0 if y < cutoffIntensity else 1, x)), imarray)))
        imarray = np.array(list(map(lambda x: list(map(lambda y: 0 if y < cutoffIntensity else math.log(y), x)), imarray)))

    score = np.add.reduce(np.add.reduce(imarray))
    if showImage:
        imarray = np.multiply(imarray, 1/100)
        nim = Image.fromarray(imarray)
        nim.show()
    return score


def getRedIntensity(im, cutoff = True, cutoffIntensity = 500, maxIntensity = 5000, showImage = False):
    im.seek(1)
    imarray = np.array(im).astype(np.int64)     #np.int64 is the fastest, probably some weird optimization numpy did
    if cutoff:
        # imarray = np.array(list(map(lambda x: list(map(lambda y: 0 if y < cutoffIntensity else y, x)), imarray)))
        # imarray = np.array(list(map(lambda x: list(map(lambda y: 0 if y < cutoffIntensity else min(maxIntensity, y), x)), imarray)))
        # imarray = np.array(list(map(lambda x: list(map(lambda y: 0 if y < cutoffIntensity else 1, x)), imarray)))
        imarray = np.array(list(map(lambda x: list(map(lambda y: 0 if y < cutoffIntensity else math.log(y), x)), imarray)))
    score = np.add.reduce(np.add.reduce(imarray))
    if showImage:
        imarray = np.multiply(imarray, 1/10)
        nim = Image.fromarray(imarray)
        nim.show()
    return score
    


    
im = Image.open("P_1_1000X.tif")

# print(getGreenIntensity(im, showImage=True))
# print(getRedIntensity(im, showImage=True))
# print(getGreenIntensity(im, cutoff = True, cutoffIntensity = 5000, showImage = True)/getRedIntensity(im, cutoff = False, cutoffIntensity = 500, showImage = True))

for filename in filenames_L:
    im = Image.open(filename)
    # print(filename, getGreenIntensity(im)/getRedIntensity(im))
    # print(filename, getRedIntensity(im))
    # print(getGreenIntensity(im, cutoff = True, cutoffIntensity = 5000)/getRedIntensity(im, cutoff = True, cutoffIntensity = 500))
    # print(getGreenIntensity(im, cutoff = True, cutoffIntensity = 5000)/getRedIntensity(im, cutoff = False, cutoffIntensity = 500))
    # print(getGreenIntensity(im, cutoff = True, cutoffIntensity = 5000)/getRedIntensity(im, cutoff = True, cutoffIntensity = 300))
    print(getGreenIntensity(im, cutoff = True, cutoffIntensity = 5000)/getRedIntensity(im, cutoff = True, cutoffIntensity = 500))
endTime = time.time()
print(f"Runtime of the program is {endTime - startTime}")
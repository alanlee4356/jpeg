import cv2
img = cv2.imread('/Users/alanlee/Downloads/jpeg-python-master/lena.bmp',cv2.IMREAD_GRAYSCALE)

thresh = 128

img_binary = cv2.threshold(img,thresh,255,cv2.THRESH_BINARY)[1]

cv2.imwrite('/Users/alanlee/Downloads/jpeg-python-master/lena_gray.bmp',img_binary)
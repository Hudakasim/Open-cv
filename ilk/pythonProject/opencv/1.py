import cv2

img=cv2.imread('2.jpg')
# img=cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE) --> B&W

# image tab control
cv2.namedWindow("image", cv2.WINDOW_NORMAL)

# (label, the photo)
cv2.imshow('image',img)

# save a copy of the image
cv2.imwrite("copy1.jpg", img)

# 0 -> wait until any key been pressed 500 -> 0.5sec 1000 -> 1 sec
cv2.waitKey(0)

cv2.destroyAllWindows()
import cv2
image = cv2.imread('puppy.jpg')
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_grey = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(inverted_grey, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)


# cv2.imshow("original", image)
# cv2.imshow("sketcher", sketch)

cv2.imwrite('puppy_sketch.jpg', sketch)

cv2.waitKey(0)
cv2.destroyAllWindows()

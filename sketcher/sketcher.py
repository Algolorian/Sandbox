import cv2

print('Type quit at any time to quit program')
while True:
    name = input('Type filename including extension "name.jpg": ')
    if name == 'quit':
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        exit()
    else:
        try:
            image = cv2.imread(name)
            grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            inverted_grey = cv2.bitwise_not(grey_img)
            blur = cv2.GaussianBlur(inverted_grey, (21, 21), 0)
            invertedblur = cv2.bitwise_not(blur)
            sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
            cv2.imwrite(f'{name[:-4]}_sketch.{name[-3:]}', sketch)
            print('Photo sketched')
        except:
            print('File not found')

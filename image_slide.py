import sys
import cv2
import glob

img_files = glob.glob('.\\image\\*.png')
if not img_files:
    print("NO Image")
    sys.exit()

cv2.namedWindow('check',cv2.WINDOW_NORMAL)
cv2.setWindowProperty('check',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

count = len(img_files)
index = 0

while True:
    img = cv2.imread(img_files[index])

    if img is None:
        print("ERROR")
        break

    cv2.imshow('check',img)
    if cv2.waitKey(3000) == 'q':
        break

    index += 1
    if index >= count :
        cv2.destroyAllWindows()
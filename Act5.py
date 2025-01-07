import cv2

img=cv2.imread("Piccolo.jpg")

pos=(150,110)

font=cv2.FONT_HERSHEY_SIMPLEX

fontScale = 1

color=(0,255,0)

thickness = 2

img=cv2.putText(img,"King Piccolo",pos,font,fontScale,color,thickness)

cv2.imshow("Piccolo",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
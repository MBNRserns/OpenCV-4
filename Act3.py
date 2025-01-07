import cv2

img = cv2.imread("Piccolo.jpg")

#top left corner of image
start_point=(0,0)

#bottom right corner of image
end_point=(300,250)

color=(0,255,0)

thickness=9

img=cv2.line(img,start_point,end_point,color,thickness)

cv2.imshow("Piccolo",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
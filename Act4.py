import cv2

img=cv2.imread("Piccolo.jpg")

start_point= (15,15)

end_point= (500,900)

color = (60,190,20)

thickness= (9)

img=cv2.rectangle(img,start_point,end_point,color,thickness)

cv2.imshow("Piccolo",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
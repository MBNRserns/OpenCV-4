import cv2

img=cv2.imread("Piccolo.jpg")



start_point= (100,400)

end_point= (430,845)

color = (60,10,100)

thickness= (-1)

img=cv2.rectangle(img,start_point,end_point,color,thickness)



start_point=(50,400)

end_point=(250,220)

color=(0,255,100)

thickness=9

img=cv2.line(img,start_point,end_point,color,thickness)



start_point=(250,220)

end_point=(470,400)

color=(0,255,100)

thickness=9



img=cv2.line(img,start_point,end_point,color,thickness)

start_point=(470,400)

end_point=(50,400)

color=(0,255,100)

thickness=9

img=cv2.line(img,start_point,end_point,color,thickness)



cv2.imshow("Piccolo",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

img=cv2.imread("Piccolo.jpg")

#Center coordinates
center_coordinates = (120,50)

#Circle Radius
radius = 20

#blue color in BGR
color = (255, 0, 0)

#Line thickness of 2px
thickness = 2

img=cv2.circle(img, center_coordinates, radius, color, thickness)

cv2.imshow("Piccolo",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
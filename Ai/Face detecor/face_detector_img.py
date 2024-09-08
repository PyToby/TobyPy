import cv2


#Load pre-trained data from opencv
face_data = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#Image to detect
img = cv2.imread('C:/Users/tobyr/TobyPy/TobyPy/Ai/Face detecor/faces_03.png')

#Haarcascade takes only grayscaled images
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect face in img
face_coordinates = face_data.detectMultiScale(gray_img)
#print(face_coordinates)

#Draw rectangles 
#(the image, (coordinates to upper right corner), (coor to bottom left corner), (color in BGR), thickness)
for x, y, w, h in face_coordinates:
    fin_img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 4)

'''
(x, y, w, h) = face_coordinates[0] --> draws around the first person
(x, y, w, h) = face_coordinates[1] --> draws around the second person
fin_img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 4) --> actually write it out
'''

#show img
cv2.imshow('Face Detector', fin_img)
#Making sure program doesn't close instantly
cv2.waitKey()

import cv2

#Load pre-trained data from opencv
face_data = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#Video capture | 0 == default webcam or put a video file
#'C:/Users/tobyr/TobyPy/TobyPy/Ai/Face detecor/199623-910995789_tiny.mp4'
video = cv2.VideoCapture(0)
key = cv2.waitKey(1)

while True:
    #read the current frame
    successful_frame_read, frame = video.read()
    
    #Haarcascade takes only grayscaled images
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect face in img
    face_coordinates = face_data.detectMultiScale(gray_frame)


    #Draw rectangles 
    #(the image, (coordinates to upper right corner), (coor to bottom left corner), (color in BGR), thickness)
    for x, y, w, h in face_coordinates:
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 4)

    #show img
    cv2.imshow('Press Esc or Q to quit', rectangle)
    #Making sure program doesn't close instantly
    key = cv2.waitKey(1)

    #press Esc or Q to quit
    if key == 81 or key == 27:
        break

video.release()
'''
(x, y, w, h) = face_coordinates[0] --> draws around the first person
(x, y, w, h) = face_coordinates[1] --> draws around the second person
fin_img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 4) --> actually write it out
'''

    

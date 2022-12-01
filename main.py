import cv2
face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_profileface.xml")


cap = cv2.VideoCapture(0)
while True:
    success,img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x + w ,y + h), (0, 255, 0),2)

        cv2.imshow('res', img)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

cap.realese()
cv2.destroyAllWindows
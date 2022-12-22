# # Вывод изображения с камеры

# import cv2

# capture = cv2.VideoCapture(0)

# while True: 
#     ret, img = capture.read()

#     cv2.imshow("Postavte 3 pozhaluista" , img)

#     k = cv2.waitKey(30) & 0xFF

#     if k == 27:
#         break
# capture.release()
# cv2.destroyAllWindows





#Каскады Хаара

# from shutil import SpecialFileError
# import cv2

# capture = cv2.VideoCapture(0) 
# face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# while True: 
#     ret, img = capture.read()

#     faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(20, 20)) #SF- размер 1.5x.  MN 5 для увеличения точности. MS - минимум размер <-Вохвращает массив лиц

#     for(x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (255,0, 0),2) # (x+w, y+h) координаты конца.

#     cv2.imshow("From Camera" , img)

#     k = cv2.waitKey(30) & 0xFF

#     if k == 27:
#         break
# capture.release()
# cv2.destroyAllWindows





# import cv2

# cap = cv2.VideoCapture(0) 
# cap.set(cv2.CAP_PROP_FPS, 24)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# codec=cv2.VideoWriter_fourcc(*'XVID')
# out=cv2.VideoWriter('out.avi', codec, 25.0,(1280, 720))

# while True:
#     ret, frame = cap.read()  #ret возвращает флаг read который T|F Frame возвращает картинку
#     cv2.imshow('Postavte 3 pozhaluista', frame)
#     out.write(frame) #Сохраняем кадры

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# out.release()
# cap.release()
# cv2.destroyAllWindows




import cv2

image = cv2.imread("img.jpg")

cv2.imshow("Kartinka",  age)
cv2.waitKey(0)
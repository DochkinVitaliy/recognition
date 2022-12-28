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









#Сохраняем в файл видео

import cv2

cap = cv2.VideoCapture(0) 
cap.set(cv2.CAP_PROP_FPS, 24)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

codec=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('out.avi', codec, 25.0,(1280, 720))

while True:
    ret, frame = cap.read()  #ret возвращает флаг read который T|F Frame возвращает картинку
    cv2.imshow('Postavte 3 pozhaluista', frame)
    out.write(frame) #Сохраняем кадры

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
out.release()
cap.release()
cv2.destroyAllWindows


#Вывод картинки

# import cv2

# image = cv2.imread("img.jpg")

# cv2.imshow("Kartinka",  image)
# cv2.waitKey(0)



#Вывод картинки в ЧБ

# import cv2

# image = cv2.imread("img.jpg")
# gray = cv2.imread("img.jpg", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("Kartinka",  image)
# cv2.imshow("Kartinka1",  gray)
# cv2.waitKey(0)




#Вывод по IP
# import cv2

# cap = cv2.VideoCapture(2) 
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





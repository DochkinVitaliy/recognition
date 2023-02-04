import cv2

def detect_motion():
    cap = cv2.VideoCapture(r'1.mp4', cv2.CAP_ANY)                           
    ret, frame = cap.read()    
    gray_capture = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                          
    window_size = 5
    sigma = 5
    new_frame = cv2.GaussianBlur(gray_capture, window_size), sigma
    h = len(gray_capture)
    w = len(gray_capture[0])

    fourcc = cv2.VideoWriter_fourcc(*'XVID')                                
    video_writer = cv2.VideoWriter("res.mov", fourcc, 25, (w, h))
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)                    
    while True:                                                            
        cv2.imshow('frame', frame)
        old_frame = new_frame                                                
        ret, frame = cap.read()                                              
        if not ret:                                                          
            break
        gray_capture = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)              
        new_frame = cv2.GaussianBlur(gray_capture,(window_size, window_size), sigma)     
        frame_dif = cv2.absdiff(old_frame, new_frame)                       
        retval, frame_dif = cv2.threshold(frame_dif, 50, 127, cv2.THRESH_BINARY)
        contours, hier = cv2.findContours(frame_dif, 
cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i in contours:                                                  
            if 200 < cv2.contourArea(i):                                    
                video_writer.write(frame)
                continue
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

detect_motion()

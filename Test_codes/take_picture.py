import cv2
# reading frames



# Checking if frame captured or not
def video():
    webcam = cv2.VideoCapture(0)
    if not webcam.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = webcam.read()
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow('Input', frame)

        c = cv2.waitKey(1)
        if isinstance(c, int) and c!=-1:
            print(c)
            break

    webcam.release()
    cv2.destroyAllWindows()

def take_photo():
    webcam = cv2.VideoCapture(0)
    ret, frame = webcam.read()
    print (ret)

    # releasing the webcam

    webcam.release()
    # displaying image

    cv2.imshow("my image", frame)
    cv2.imwrite('H:\Face_recognition\photos\opencv1.png', frame)
    # stopping the output

    cv2.waitKey()

    # releasing all windows

    cv2.destroyAllWindows()

video()
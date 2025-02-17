import cv2
import numpy as np

 # Inisialisasi kamera
cap = cv2.VideoCapture(0)

while True:
 _, frame = cap.read()
 hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

 # Rentang warna biru dalam HSV
 lower_blue = np.array([100, 150, 50])
 upper_blue = np.array([140, 255, 255])

 # Masking untuk mendeteksi warna biru
 mask = cv2.inRange(hsv, lower_blue, upper_blue)
 result = cv2.bitwise_and(frame, frame, mask=mask)

 # menemukan kontur
 contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

 for contour in contours:
    if cv2.contourArea(contour) > 500: #Filter kontur kecil
       x, y, w, h = cv2.boundingRect(contour)
       cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
       cv2.putText(frame, "biru", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0),)
 # Menampilkan hasil
 cv2.imshow("Frame", frame)
 cv2.imshow("Mask", mask)
 cv2.imshow("Result", result)

 if cv2.waitKey(1) & 0xFF == ord('q'):
     break
 
cap.release()
cv2.destroyAllWindows()
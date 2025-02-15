import cv2
import numpy as np
# Inisialisasi kamera
cap = cv2.VideoCapture(0)
while True:
 _, frame = cap.read()
 hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 # Rentang warna blue dalam HSV
 lower_blue= np.array([100, 150, 70])
 upper_blue = np.array([140, 255, 255])
 # Masking untuk mendeteksi warna merah
 mask = cv2.inRange(hsv, lower_blue, upper_blue)
 result = cv2.bitwise_and(frame, frame, mask=mask)
 # Menampilkan hasil
 cv2.imshow("Frame", frame)
 cv2.imshow("Mask", mask)
 cv2.imshow("Result", result)
 if cv2.waitKey(1) & 0xFF == ord('q'):
  break
cap.release()
cv2.destroyAllWindows()
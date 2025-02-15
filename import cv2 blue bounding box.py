import cv2
import numpy as np

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Kamera tidak dapat diakses")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:  
        print("Error: Frame tidak terbaca")
        break

    # Konversi ke HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Rentang warna biru dalam HSV
    lower_blue = np.array([100, 150, 70])
    upper_blue = np.array([140, 255, 255])

    # Membuat mask untuk mendeteksi warna biru
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Menemukan kontur (tepi objek biru)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Gambar bounding box di sekitar objek biru yang terdeteksi
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Filter kontur kecil agar tidak terdeteksi sebagai noise
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Gambar kotak hijau

    # Menampilkan hasil
    cv2.imshow("Frame (Original with Bounding Box)", frame)
    cv2.imshow("Mask (Blue Detected)", mask)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Membersihkan sumber daya
cap.release()
cv2.destroyAllWindows()

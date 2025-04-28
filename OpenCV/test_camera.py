import cv2

# Coba buka kamera index 0
cap = cv2.VideoCapture(4)

if not cap.isOpened():
    print("❌ Kamera GAGAL dibuka (index 0)")
else:
    print("✅ Kamera BERHASIL dibuka (index 0)")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Frame gagal diambil.")
            break

        cv2.imshow('Test Kamera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

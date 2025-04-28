import cv2

def find_available_camera(max_index=10):
    for index in range(max_index):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            print(f"✅ Kamera ditemukan di index: {index}")
            cap.release()
            return index
        cap.release()
    print("❌ Tidak ada kamera yang ditemukan.")
    return None

# Cari kamera yang aktif
camera_index = find_available_camera()

if camera_index is not None:
    cap = cv2.VideoCapture(camera_index)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Gagal mengambil frame.")
            break

        cv2.imshow('Kamera Aktif', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
else:
    print("🚨 Gagal menemukan kamera. Pastikan kamera terpasang dan aktif.")

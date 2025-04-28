from ultralytics import YOLO
import cv2

# Load model YOLOv8 (pretrained)
model = YOLO("yolov8n.pt")  # kecil, cepat

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

# Cari kamera aktif
camera_index = find_available_camera()

# Kalau ketemu kamera
if camera_index is not None:
    cap = cv2.VideoCapture(camera_index)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Gagal ambil gambar dari kamera.")
            break

        # Deteksi objek di frame
        results = model.predict(source=frame, save=False, conf=0.5)

        # Gambar hasil deteksi
        annotated_frame = results[0].plot()

        # Tampilkan ke layar
        cv2.imshow("YOLOv8 Detection", annotated_frame)

        # Tekan 'q' buat keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
else:
    print("🚨 Kamera tidak ditemukan.")

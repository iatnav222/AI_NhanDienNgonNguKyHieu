# Đồ án Nhận Diện Quần Áo Theo Thời Gian Thực (Fashion Object Detection)

## 📌 Giới thiệu chung
Đây là đồ án kết thúc học phần A.I, tập trung vào việc áp dụng công nghệ Thị giác Máy tính (Computer Vision) để nhận diện và định vị các loại quần áo trên người dùng thông qua camera thời gian thực.

## 🎯 Mục tiêu
Hệ thống sẽ sử dụng thuật toán Học sâu (Deep Learning) - cụ thể là mô hình **YOLO (You Only Look Once)** để quét hình ảnh từ webcam, sau đó:
1. Phát hiện (Detect) vị trí các món đồ (áo, quần) đang được mặc.
2. Vẽ khung chữ nhật (Bounding box) bao quanh món đồ.
3. Hiển thị tên loại quần áo (Label) kèm theo độ tin cậy (Confidence score).

## 🛠 Công nghệ sử dụng (Tech Stack)
- **Ngôn ngữ:** Python
- **Mô hình AI:** YOLOv8 (từ Ultralytics) - Mô hình object detection tiên tiến, nhẹ và cực nhanh.
- **Thư viện AI/Xử lý ảnh:** PyTorch, OpenCV.
- **Giao diện & Backend:** Flask (Web Framework), HTML/CSS/JS.

## 🚀 Các tính năng dự kiến
- Nhận diện realtime thông qua luồng webcam.
- Nhận diện ảnh tĩnh (Upload ảnh lên và nhận diện).
- Hỗ trợ nhận diện các loại trang phục cơ bản (ví dụ: Áo thun, Sơ mi, Áo khoác, Quần dài, Quần ngắn).

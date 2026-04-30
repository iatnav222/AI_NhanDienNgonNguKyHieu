# Đồ án Nhận Diện Ngôn Ngữ Ký Hiệu Tay (Sign Language Recognition)

## 📌 Giới thiệu chung
Đây là đồ án kết thúc học phần A.I, tập trung vào việc áp dụng công nghệ Thị giác Máy tính (Computer Vision) để nhận diện ngôn ngữ ký hiệu tay (hệ chữ cái ASL) thông qua camera thời gian thực, giúp hỗ trợ giao tiếp cho người khiếm thính.

## 🎯 Mục tiêu
Hệ thống sẽ sử dụng thuật toán Học sâu (Deep Learning) - cụ thể là mô hình **YOLOv8** để:
1. Phát hiện (Detect) vị trí bàn tay trước webcam.
2. Phân loại (Classify) hình dáng bàn tay đó tương ứng với chữ cái nào (A, B, C...).
3. Hiển thị chữ cái nhận diện được lên màn hình.

## 🛠 Công nghệ sử dụng
- **Ngôn ngữ:** Python
- **Mô hình AI:** YOLOv8 (từ Ultralytics)
- **Thư viện AI/Xử lý ảnh:** PyTorch, OpenCV.
- **Giao diện & Backend:** Flask (Web Framework), HTML/CSS/JS.

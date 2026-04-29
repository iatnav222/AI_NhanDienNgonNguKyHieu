# Kiến Trúc Hệ Thống (System Architecture)

## 1. Cấu trúc thư mục dự kiến
Khi làm dự án, thư mục của bạn nên được tổ chức rõ ràng như sau:
```text
IP_Action/
├── datasets/            # Nơi chứa ảnh để huấn luyện AI (sẽ tải về sau)
├── models/              # Nơi chứa file model AI sau khi train xong (.pt)
├── static/              # Chứa CSS, JavaScript, Hình ảnh cho giao diện Web
├── templates/           # Chứa các file HTML (giao diện web)
├── app.py               # File chạy server Flask (Cầu nối giữa Web và AI)
├── train_model.ipynb    # File Jupyter Notebook dùng để viết code huấn luyện AI
├── requirements.txt     # Danh sách các thư viện cần cài đặt
├── README.md            # Mô tả tổng quan đồ án
├── ARCHITECTURE.md      # Mô tả kiến trúc đồ án (File bạn đang đọc)
└── ROADMAP.md           # Các bước thực hiện dự án
```

## 2. Luồng hoạt động (Data Flow)
Hệ thống hoạt động theo quy trình 3 bước khép kín:

1. **Client (Trình duyệt Web/Giao diện):** 
   - Truy cập vào trang web `http://localhost:5000`.
   - Trang web sẽ hiển thị luồng Video/Webcam đã được xử lý.
2. **Backend (Flask - `app.py`):** 
   - Đọc từng khung hình ảnh (frame) từ Webcam thông qua OpenCV.
   - Gửi hình ảnh đó vào bộ máy AI (YOLOv8) để phân tích.
3. **AI Engine (YOLOv8):** 
   - YOLOv8 phân tích và trả về tọa độ khung (Bounding box) + Nhãn (Ví dụ: T-shirt, Pants...).
   - Backend dùng OpenCV vẽ khung màu lên ảnh, nén ảnh lại và stream liên tục lên giao diện Web.

## 3. Lý do chọn YOLOv8
Thay vì dùng 2 mô hình phức tạp (như đồ án nhận diện hành động cũ cần 1 mô hình tìm người + 1 mô hình phân loại hành động), YOLOv8 là mô hình **"Tất cả trong một"**. Nó có thể vừa định vị vị trí cái áo trên bức hình, vừa phân loại xem cái áo đó là loại gì trong cùng 1 bước duy nhất (One-stage detector). Điều này giúp hệ thống nhẹ và chạy mượt mà trên webcam.

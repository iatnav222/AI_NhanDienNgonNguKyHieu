# DRAFT BÁO CÁO: NHẬN DIỆN NGÔN NGỮ KÝ HIỆU (YOLOv8)

*(Đây là file khung, sẽ được cập nhật và điền nội dung liên tục trong quá trình làm đồ án)*

## Chương 1: Tổng quan về Nhận diện Ngôn ngữ Ký hiệu
### 1.1 Tổng quan về mô hình AI sử dụng trong đề tài
- **[CẦN LÀM]:** Viết đoạn văn giới thiệu về kiến trúc YOLOv8. Nêu ưu thế tốc độ thời gian thực (Real-time).

### 1.2 Mô hình triển khai (Deploy)
- **[CẦN LÀM]:** Vẽ sơ đồ triển khai (Webcam -> Flask -> YOLO -> Browser & SQLite).

---

## Chương 2: Xây dựng Hệ thống
### 2.1 Kiến trúc hệ thống
- **[CẦN LÀM]:** Viết mô tả bằng lời giải thích sự tương tác giữa Frontend (HTML/JS), Backend (Flask) và Cơ sở dữ liệu.

### 2.2 Cơ sở dữ liệu
- **[CẦN LÀM]:** Chèn hình ảnh bảng mô tả CSDL SQLite. Bảng `History` gồm 3 cột: `id` (Khóa chính), `text_content` (Nội dung câu đã dịch), `created_at` (Thời gian lưu).

### 2.3 Giao diện đề tài
- **[CẦN LÀM]:** Chụp ảnh màn hình giao diện web (Cần thấy rõ khu vực Webcam và khu vực Bảng Lịch sử) dán vào đây.

### 2.4 Cài đặt & Kỹ thuật kết nối
- **[CẦN LÀM]:** Dán các đoạn code quan trọng giải thích cơ chế Flask stream video qua hàm `yield` và code Python kết nối với SQLite (`import sqlite3`).

---

## Chương 3: Mô hình sử dụng trong đề tài
### 3.1 Ngữ liệu huấn luyện (Dataset)
- **[CẦN LÀM]:** Trình bày thông số bộ Dataset (Số lượng ảnh, Các nhãn A-Z, Tỷ lệ chia Train/Test). Chụp ảnh minh họa Dataset.

### 3.2 Quá trình huấn luyện
- **[CẦN LÀM]:** Cung cấp cấu hình huấn luyện (Epochs, Batch size, Optimizer). Dán mã nguồn (code) dùng để train mô hình trên Colab vào báo cáo.

### 3.3 Kết quả - đánh giá & độ chính xác
- **[CẦN LÀM]:** Sau khi train xong, copy các biểu đồ `Confusion Matrix`, `F1-Curve`, thông số `mAP50` dán vào đây để chứng minh độ chính xác.

### 3.4 Tích hợp Mô hình vào Đề tài
- **[CẦN LÀM]:** Dán mã nguồn của file `app.py`. Chỉ rõ từng dòng code:
  - Code load mô hình: `model = YOLO('best.pt')`
  - Code đọc khung hình và đưa vào đoán: `results = model.predict(frame)`
  - Code lấy kết quả vẽ khung chữ nhật lên video.

---

## Chương 4: Tài liệu tham khảo
- **[CẦN LÀM]:** Khi hoàn thiện, bổ sung tài liệu tham khảo theo chuẩn IEEE (Sách, Web, Paper về YOLOv8).

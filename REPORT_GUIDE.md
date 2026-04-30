# HƯỚNG DẪN LÀM BÁO CÁO VÀ GIẢI ĐÁP THẮC MẮC

Dưới đây là giải đáp cho các (Ý kiến cá nhân) mà bạn đã note trong file `.txt`:

### 1. Mô hình và API AI khác nhau như thế nào? Nên chọn cái nào?
- **API AI:** Là dịch vụ của các công ty lớn (như Google Vision, ChatGPT) đã làm sẵn. Bạn gửi ảnh lên server của họ, họ trả về kết quả. Rất nhàn, nhưng **không thể hiện được kỹ năng AI**, dễ bị trừ điểm vì "chỉ biết gọi hàm có sẵn".
- **Mô hình AI (Model):** Là bạn tải thuật toán (YOLOv8) về máy, **TỰ MÌNH** đi kiếm dữ liệu (ảnh bàn tay), **TỰ MÌNH** huấn luyện (train).
👉 **Đề xuất của tôi:** Đồ án của bạn 100% sử dụng **Mô hình AI (YOLOv8)**. Trong báo cáo, bạn hãy xóa bỏ các chữ "API", chỉ tập trung viết về "Mô hình".

### 2. Mô hình này phù hợp xử lý bài toán nào? (Chương 1.1)
- YOLOv8 là mô hình Object Detection dạng One-stage (xử lý trong 1 bước). Nó hy sinh một chút độ chuẩn xác để đổi lấy **Tốc độ cực nhanh**. Do đó, nó sinh ra là để xử lý bài toán **Nhận diện theo thời gian thực qua Video/Webcam** (Real-time).

### 3. Thiết kế kiến trúc như thế nào? (Chương 2.1)
- Ở chương này, ta sẽ vẽ một biểu đồ các khối: [Webcam] -> [Giao diện HTML] -> [Flask Backend] <-> [Database SQLite] & [Mô hình YOLOv8]. Tôi sẽ nhắc bạn vẽ cái này sau.

### 4. Cơ sở dữ liệu (Database) cần phải làm gì? Dùng MySQL được không? (Chương 2.2)
- **Quyết định chính thức:** Để được điểm cao ở phần cấu trúc báo cáo, chúng ta SẼ LÀM DATABASE, nhưng sử dụng **SQLite** (tích hợp sẵn trong Python, cực nhẹ, không cần cài MySQL rườm rà).
- **Chức năng:** Làm tính năng **Lưu lịch sử dịch thuật**. Mỗi khi AI ghép thành công 1 câu từ ký hiệu tay, người dùng bấm "Lưu", câu đó sẽ được chèn vào database kèm thời gian, và hiển thị lại ở một bảng trên giao diện web.

### 5. Kỹ thuật kết nối (Chương 2.4) là sao?
- Kỹ thuật kết nối ở đây chính là đoạn code Python sử dụng thư viện `sqlite3` để mở file CSDL và chèn dữ liệu `INSERT INTO History...`. Ta sẽ dán đoạn code đó vào chương này để chứng minh sinh viên có biết thao tác với Database.

### 6. Ngữ liệu huấn luyện cần phải làm gì? (Chương 3.1)
- Viết ra: Dataset lấy từ đâu (Roboflow), có bao nhiêu tấm ảnh, chia làm mấy tập (Train/Test/Valid) với tỷ lệ bao nhiêu, có bao nhiêu nhãn (26 chữ cái). Sau đó dán vài tấm ảnh minh họa bàn tay vào.

### 7. Đánh giá và độ chính xác dựa vào đâu? (Chương 3.3)
- YOLOv8 sẽ **TỰ ĐỘNG sinh ra các file ảnh biểu đồ** (mAP, F1-Curve, Confusion Matrix) sau khi train. Bạn chỉ việc lấy các ảnh biểu đồ đó copy dán vào báo cáo, ghi chú: "Theo biểu đồ trên, độ chính xác đạt X%" là ăn điểm tuyệt đối.

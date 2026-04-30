# HƯỚNG DẪN LÀM BÁO CÁO VÀ GIẢI ĐÁP THẮC MẮC

Dưới đây là giải đáp cho các (Ý kiến cá nhân) mà bạn đã note trong file `.txt`:

### 1. Mô hình và API AI khác nhau như thế nào? Nên chọn cái nào?
- **API AI:** Là dịch vụ của các công ty lớn (như Google Vision, ChatGPT) đã làm sẵn. Bạn chỉ cần gửi ảnh lên server của họ qua Internet, họ trả về kết quả. Rất nhàn, nhưng **không thể hiện được kỹ năng AI của sinh viên**, dễ bị thầy cô trừ điểm vì "chỉ biết gọi hàm có sẵn".
- **Mô hình AI (Model):** Là bạn tải thuật toán (YOLOv8) về máy, **TỰ MÌNH** đi kiếm dữ liệu (ảnh bàn tay), **TỰ MÌNH** huấn luyện (train).
👉 **Đề xuất của tôi:** Đồ án của bạn 100% sử dụng **Mô hình AI (YOLOv8)**. Trong báo cáo, bạn hãy xóa bỏ các chữ "API", chỉ tập trung viết về "Mô hình" thôi nhé.

### 2. Mô hình này phù hợp xử lý bài toán nào? (Chương 1.1)
- Bạn sẽ giải thích YOLOv8 là một mô hình Object Detection (Nhận diện đối tượng) dạng One-stage (xử lý trong 1 bước). Nó hy sinh một chút xíu độ chuẩn xác để đổi lấy **Tốc độ cực nhanh**. Do đó, nó sinh ra là để xử lý bài toán **Nhận diện theo thời gian thực qua Video/Webcam** (Real-time).

### 3. Thiết kế kiến trúc như thế nào? (Chương 2.1)
- Ở chương này, ta sẽ dùng công cụ (như Draw.io) để vẽ một biểu đồ các khối vuông: [Webcam] -> [Giao diện HTML] -> [Flask Backend] -> [Mô hình YOLOv8]. Tôi sẽ nhắc bạn vẽ cái này sau khi làm xong web.

### 4. Cơ sở dữ liệu (Database) cần phải làm gì? Dùng MySQL được không? (Chương 2.2)
- **Ý kiến của tôi:** Một hệ thống AI nhận diện bằng webcam cơ bản thì **KHÔNG CẦN Cơ Sở Dữ Liệu**. Dữ liệu của AI là file mô hình (`best.pt`) và tập ảnh (`dataset`), không phải là bảng biểu quan hệ như Web bán hàng. 
- **Cách xử lý:** Nếu giáo viên dễ tính, bạn có thể xin phép xóa hẳn phần CSDL khỏi báo cáo. Tuy nhiên, nếu giáo viên BẮT BUỘC phải có MySQL để chấm điểm môn, ta sẽ "chế" thêm chức năng: **Lưu lịch sử dịch thuật**. (Cứ mỗi khi AI nhận diện ra 1 từ, nó sẽ lưu từ đó vào MySQL kèm thời gian). Cái này làm bằng MySQL rất dễ, tôi sẽ hướng dẫn code sau.

### 5. Kỹ thuật kết nối (Chương 2.4) là sao?
- Nếu chốt làm MySQL (như nói ở trên), thì kỹ thuật kết nối ở đây chính là việc dùng thư viện Python (như `mysql-connector-python`) để chèn dữ liệu vào bảng. Ta sẽ dán đoạn code đó vào báo cáo.

### 6. Ngữ liệu huấn luyện cần phải làm gì? (Chương 3.1)
- Cần viết ra: Dataset của bạn lấy từ đâu (Roboflow), có bao nhiêu tấm ảnh, chia làm mấy tập (Train/Test/Valid) với tỷ lệ bao nhiêu, có bao nhiêu nhãn (26 chữ cái). Sau đó cắt vài tấm ảnh minh họa bàn tay dán vào báo cáo.

### 7. Đánh giá và độ chính xác dựa vào đâu? (Chương 3.3)
- Cực kỳ đơn giản! Trong AI, bạn KHÔNG tự đoán độ chính xác. Khi bạn ấn nút Train xong, hệ thống YOLOv8 sẽ **TỰ ĐỘNG sinh ra các file ảnh biểu đồ** (mAP, F1-Curve, Confusion Matrix). Bạn chỉ việc lấy các ảnh biểu đồ đó copy dán vào báo cáo, ghi chú: "Theo biểu đồ trên, độ chính xác đạt 95%" là xong, ăn điểm tuyệt đối về tính khoa học.

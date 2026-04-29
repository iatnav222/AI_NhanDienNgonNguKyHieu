# Lộ Trình Thực Hiện (Roadmap)
Dưới đây là danh sách các việc (Task) bạn cần làm để hoàn thành đồ án từ con số 0. Hãy bám sát các bước này.

## Giai đoạn 1: Chuẩn bị Dữ liệu (Quan trọng nhất) - Tuần 1
- [ ] Xác định danh sách các loại quần áo cần nhận diện (Class list). Gợi ý 5 nhãn phổ biến: `t-shirt` (áo thun), `shirt` (áo sơ mi), `jacket` (áo khoác), `pants` (quần dài), `shorts` (quần ngắn).
- [ ] Truy cập **Roboflow Universe** (universe.roboflow.com) hoặc **Kaggle**, tìm kiếm với từ khóa `"clothing object detection yolov8"` hoặc `"fashion yolov8 dataset"`.
- [ ] Tải dataset về máy. (Lưu ý chọn định dạng YOLOv8).

## Giai đoạn 2: Huấn luyện Mô hình AI (Training) - Tuần 2
- [ ] Tạo file `train_model.ipynb` (Nên dùng Google Colab để train nếu máy tính không có Card màn hình mạnh).
- [ ] Cài đặt thư viện: `pip install ultralytics opencv-python`.
- [ ] Viết code để đưa tập dữ liệu (dataset) vào mô hình YOLOv8n (bản nano nhẹ nhất).
- [ ] Chạy huấn luyện (Train) mô hình (thường mất 1-3 tiếng tùy lượng ảnh).
- [ ] Lấy file kết quả mô hình đã được huấn luyện xong (thường có tên `best.pt`) và thả vào thư mục `models/` của dự án.

## Giai đoạn 3: Viết Backend & Kết nối AI - Tuần 3
- [ ] Viết file `app.py` để khởi tạo server Flask đơn giản.
- [ ] Thêm thư viện AI vào file `app.py`, load file `best.pt`.
- [ ] Viết hàm đọc hình từ webcam và đưa vào mô hình dự đoán thử (`model.predict()`).
- [ ] Vẽ khung (box) lên hình ảnh và đưa hình ảnh đó lên API streaming.

## Giai đoạn 4: Thiết kế Giao diện Web (UI) - Tuần 4
- [ ] Tạo file `index.html` trong thư mục `templates/`.
- [ ] Tạo file `style.css` trong thư mục `static/`.
- [ ] Nhúng luồng video từ Flask vào thẻ `<img src="/video_feed" />` trên giao diện web.
- [ ] Thiết kế giao diện hiện đại, trực quan (có thể tham khảo màu sắc và phong cách UI đẹp mắt).

## Giai đoạn 5: Tối ưu & Viết Báo Cáo
- [ ] Test thử với nhiều loại áo quần ngoài đời thật qua webcam.
- [ ] (Tùy chọn) Thêm chức năng cho phép upload ảnh tĩnh lên để nhận diện.
- [ ] Viết báo cáo: Mô tả về YOLOv8, lý do chọn mô hình, nguồn dataset, và kết quả thực tế.
- [ ] Trình diễn và báo cáo cuối kỳ.

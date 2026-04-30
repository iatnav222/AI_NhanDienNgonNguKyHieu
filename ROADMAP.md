# Lộ Trình Thực Hiện (Roadmap) - Ngôn Ngữ Ký Hiệu

## Giai đoạn 1: Chuẩn bị Dữ liệu (Dataset) - [ĐÃ HOÀN THÀNH ✅]
- [x] Lên **Roboflow Universe** tìm bộ dataset.
- [x] Lấy code tải Dataset thẳng lên Google Colab.

## Giai đoạn 2: Huấn luyện Mô hình AI (Training) - [ĐÃ HOÀN THÀNH ✅]
- [x] Thiết lập Google Colab với GPU T4.
- [x] Train mô hình YOLOv8 trên bộ dữ liệu bàn tay.
- [x] Thu hoạch file bộ não AI (`best.pt`) và các file biểu đồ kết quả (`confusion_matrix.png`, `results.png`).

## Giai đoạn 3: Viết Backend & Kết nối AI - [ĐÃ HOÀN THÀNH ✅]
- [x] Viết `app.py` để chạy máy chủ Flask.
- [x] Khởi tạo CSDL SQLite (`database.db`) lưu lịch sử.
- [x] Load file `best.pt` vào OpenCV để nhận diện qua luồng Webcam.

## Giai đoạn 4: Thiết kế Giao diện Web (UI) - [ĐÃ HOÀN THÀNH ✅]
- [x] Thiết kế trang web `index.html` hiển thị video.
- [x] Viết file `style.css` tạo giao diện chuẩn hiện đại.
- [x] Tích hợp tính năng bấm nút "Thêm chữ", "Dấu cách", và "Lưu Câu" xuống Database.

## Giai đoạn 5: Viết Báo Cáo & Demo - [ĐÃ HOÀN THÀNH ✅]
- [x] Chạy thử ứng dụng bằng lệnh `python app.py`.
- [x] Đứng trước màn hình, giơ tay làm ký hiệu để test thử độ nhạy của AI.
- [x] Chụp màn hình trang web lúc đang nhận diện và chèn vào file `MAIN_REPORT_DRAFT.md`.
- [x] Copy các biểu đồ tải từ Colab ném vào chương Đánh giá của file `MAIN_REPORT_DRAFT.md`.
- [x] Quay một đoạn video demo nhỏ chuẩn bị cho buổi báo cáo.


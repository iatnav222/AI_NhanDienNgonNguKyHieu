# Lộ Trình Thực Hiện (Roadmap) - Ngôn Ngữ Ký Hiệu

## Giai đoạn 1: Chuẩn bị Dữ liệu (Dataset)
- [ ] Lên **Roboflow Universe** tìm bộ dataset "American Sign Language Letters YOLOv8".
- [ ] Tải dataset về máy.

## Giai đoạn 2: Huấn luyện Mô hình AI (Training)
- [ ] Tạo file `train_model.ipynb` trên Google Colab.
- [ ] Train mô hình YOLOv8 trên bộ dữ liệu bàn tay vừa tải.
- [ ] Lưu file bộ não AI sau khi học xong (`best.pt`).

## Giai đoạn 3: Viết Backend & Kết nối AI
- [ ] Viết `app.py` chạy server Flask.
- [ ] Load file `best.pt` vào OpenCV để nhận diện qua luồng Webcam.

## Giai đoạn 4: Thiết kế Giao diện Web (UI)
- [ ] Thiết kế trang web `index.html` hiển thị video.
- [ ] (Nâng cao) Ghép các chữ cái nhận diện được thành chuỗi văn bản hoàn chỉnh.

## Giai đoạn 5: Báo cáo
- [ ] Bám sát theo file `MAIN_REPORT_DRAFT.md` để hoàn thành quyển báo cáo.

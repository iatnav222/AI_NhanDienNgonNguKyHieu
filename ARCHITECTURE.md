# Kiến Trúc Hệ Thống

## 1. Cấu trúc thư mục
```text
Model_AI/
├── datasets/            # Nơi chứa ảnh bàn tay (ASL) để huấn luyện AI
├── models/              # Nơi chứa file model AI sau khi train xong (best.pt)
├── static/              # Chứa CSS, JavaScript cho giao diện Web
├── templates/           # Chứa các file HTML
├── app.py               # File chạy server Flask (Cầu nối giữa Web và AI)
├── database.db          # [MỚI] File cơ sở dữ liệu SQLite lưu lịch sử giao tiếp
├── train_model.ipynb    # File code huấn luyện AI
├── requirements.txt     
├── README.md            
├── ARCHITECTURE.md      
├── ROADMAP.md           
├── REPORT_GUIDE.md      # Giải thích và hướng dẫn làm báo cáo
└── MAIN_REPORT_DRAFT.md # Khung báo cáo chính thức (Cập nhật song song)
```

## 2. Luồng hoạt động (Data Flow)
1. **Client (Web):** Bật webcam, truyền video và nhận kết quả. Bấm nút "Lưu câu" khi muốn lưu.
2. **Backend (Flask):** 
   - Lấy từng khung hình (frame), đưa vào mô hình YOLOv8.
   - Nhận lệnh "Lưu câu", chèn dữ liệu vào file `database.db` (SQLite).
3. **AI Engine (YOLOv8):** Tìm vị trí bàn tay, đoán chữ cái (ví dụ: "A"), gửi kết quả lại cho Backend để vẽ viền lên hình và stream ngược về Web.
4. **Database (SQLite):** Lưu trữ và truy xuất lịch sử các câu đã được dịch.

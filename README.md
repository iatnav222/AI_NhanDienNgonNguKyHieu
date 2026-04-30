# Đồ án Nhận Diện Ngôn Ngữ Ký Hiệu Tay (Sign Language Recognition)

## 📌 Giới thiệu chung
Đây là đồ án kết thúc học phần A.I, tập trung vào việc áp dụng công nghệ Thị giác Máy tính (Computer Vision) để nhận diện ngôn ngữ ký hiệu tay (hệ chữ cái ASL) thông qua camera thời gian thực, giúp hỗ trợ giao tiếp cho người khiếm thính.

## 🎯 Mục tiêu
Hệ thống sử dụng thuật toán Học sâu (Deep Learning) - cụ thể là mô hình **YOLOv8** để:
1. Phát hiện (Detect) vị trí bàn tay trước webcam.
2. Phân loại (Classify) hình dáng bàn tay đó tương ứng với chữ cái nào (A, B, C...).
3. Nối các chữ cái thành câu hoàn chỉnh và lưu vào Cơ sở dữ liệu SQLite.

## 🛠 Công nghệ sử dụng
- **Ngôn ngữ:** Python 3
- **Mô hình AI:** YOLOv8 (từ Ultralytics)
- **Computer Vision:** OpenCV
- **Backend & Database:** Flask (Web Framework), SQLite
- **Frontend:** HTML / CSS (Vanilla) / JS

---

## 🚀 Hướng dẫn Cài đặt & Chạy dự án (Dành cho máy mới)

### Bước 1: Yêu cầu hệ thống (Prerequisites)
- Máy tính phải được cài đặt sẵn **Python** (Khuyến nghị bản 3.9 trở lên).
- **[QUAN TRỌNG]:** Khi cài đặt Python trên Windows, hãy đảm bảo bạn đã tích vào ô vuông **`Add Python to PATH`** ở màn hình cài đặt đầu tiên. Nếu quên tích, Terminal sẽ báo lỗi không nhận diện được chữ "python".

### Bước 2: Tải dự án và Cài đặt thư viện
1. Tải toàn bộ mã nguồn của kho lưu trữ này về máy và giải nén.
2. Mở phần mềm Terminal (Command Prompt, PowerShell hoặc Terminal của VS Code) tại thư mục chứa dự án.
3. Gõ lệnh sau để cài đặt tất cả các thư viện cần thiết cho AI và Web:
   ```bash
   pip install -r requirements.txt
   ```

### Bước 3: Đảm bảo có file Mô hình AI (Trọng số)
- Đảm bảo rằng bạn đã có file **`best.pt`** (Bộ não AI sau khi đã được huấn luyện bằng Google Colab).
- File `best.pt` phải được đặt ĐÚNG VỊ TRÍ bên trong thư mục `models/`. 
- *(Đường dẫn chuẩn: `models/best.pt`)*

### Bước 4: Khởi chạy Ứng dụng
1. Từ Terminal đang mở tại thư mục dự án, chạy lệnh khởi động máy chủ Web (Flask):
   ```bash
   python app.py
   ```
   *(Nếu bị lỗi từ khóa python, hãy thử dùng lệnh `py app.py` hoặc `python3 app.py`)*

2. Mở trình duyệt Web (Chrome, Edge, Cốc Cốc...) và truy cập vào địa chỉ:
   👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

3. Cấp quyền truy cập Camera trên trình duyệt và bắt đầu trải nghiệm!

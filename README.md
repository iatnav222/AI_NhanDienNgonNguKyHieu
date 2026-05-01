# Hướng dẫn Train Dataset

Tài liệu hướng dẫn quy trình train dataset trên Google Colab

### Bước 1: Chuẩn bị môi trường Colab
1. Truy cập vào **[Google Colab](https://colab.research.google.com/)** và tạo một "Sổ tay mới" (New Notebook).
2. **Bật GPU, Cực kỳ quan trọng:**  Trên thanh menu Colab, chọn **Runtime** -> **Change runtime type** -> Tại mục *Hardware accelerator*, chọn **T4 GPU** rồi bấm Save.

### Bước 2: Tải bộ dataset
Tạo một ô code (code cell) đầu tiên, dán đoạn mã dưới và chạy để tải dataset (đợi chạy xong chuyển sang bước 3)

```python
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="B6mYXwzEAZfT2DxJdWBq")
project = rf.workspace("project-g6oev").project("trash-s8fg7")
version = project.version(5)
dataset = version.download("yolov8")
```
### Bước 3: Cài đặt thư viện
Tạo một ô code mới (bấm biểu tượng `+ Code`), dán lệnh sau vào và chạy. Cài đặt công cụ train và cấu hình

```python
%pip install ultralytics
import ultralytics
ultralytics.checks()
```

### Bước 4: Chạy lệnh Train mô hình
Tạo thêm một ô code, dán đoạn mã dưới vào để chạy. Quá trình train mất khoảng 3 tiếng.

```python
from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model.train(data=f"{dataset.location}/data.yaml", epochs=100, imgsz=640)
```

### Bước 5: Nén Thư Mục
Sau khi quá trình huấn luyện kết thúc, toàn bộ kết quả train được lưu trong thư mục `runs/`.
Tạo ô code cuối cùng và chạy đoạn mã phía dưới để nén toàn bộ file train lại:

```python
import shutil
shutil.make_archive('ket_qua_train', 'zip', 'runs')
```

**Cách tải về:**
1. Nhìn sang thanh công cụ biểu tượng "Thư mục" (Files) ở bên trái màn hình Colab.
2. Tìm file có tên là **`ket_qua_train.zip`** (refresh nếu chưa thấy)
3. Bấm vào biểu tượng dấu 3 chấm cạnh file -> Chọn **Download**.

---

### *Lưu Ý Cực Kỳ Quan Trọng
**Tránh tình trạng treo máy :** Google Colab có cơ chế tự động ngắt kết nối nếu tab trình duyệt nhàn rỗi quá lâu (không có tương tác chuột/phím trong khoảng 90 phút). Do thời gian chạy khá dài, cứ khoảng 30-45 phút cần mở lại tab Colab, thực hiện các thao tác như lăn chuột hoặc click vào màn hình để duy trì kết nối. Nếu bị ngắt giữa chừng, toàn bộ quá trình huấn luyện sẽ phải thực hiện lại từ đầu!

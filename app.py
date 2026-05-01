import os
import cv2
import sqlite3
from flask import Flask, render_template, Response, request, jsonify
from ultralytics import YOLO

app = Flask(__name__)

# --- 1. KHỞI TẠO CƠ SỞ DỮ LIỆU (SQLITE) ---
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS History (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text_content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# --- 2. LOAD MÔ HÌNH AI YOLOv8 ---
model_path = os.path.join('models', 'best.pt')
if os.path.exists(model_path):
    model = YOLO(model_path)
    print("Đã tải thành công mô hình AI!")
else:
    model = None
    print("CẢNH BÁO: Không tìm thấy file models/best.pt. Web vẫn chạy nhưng luồng camera sẽ không có AI.")

camera = None
latest_text = ""

# --- 3. XỬ LÝ HÌNH ẢNH WEBCAM & NHẬN DIỆN ---
def generate_frames():
    global latest_text, camera
    while True:
        if camera is None or not camera.isOpened():
            break
        success, frame = camera.read()
        if not success:
            break
        else:
            if model:
                # Chạy mô hình trên khung hình hiện tại (ngưỡng tin cậy 50%)
                results = model.predict(frame, conf=0.5, verbose=False)
                
                current_letter = ""
                for r in results:
                    boxes = r.boxes
                    for box in boxes:
                        # Vẽ khung Bounding Box quanh bàn tay
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        
                        # Lấy nhãn chữ cái (Ví dụ: A, B, C...)
                        cls_id = int(box.cls[0])
                        class_name = model.names[cls_id]
                        current_letter = class_name
                        
                        # Ghi chữ lên màn hình camera
                        cv2.putText(frame, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                
                if current_letter:
                    latest_text = current_letter

            # Mã hóa khung hình gửi về trình duyệt Web
            ret, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

# --- 4. CÁC API CHO GIAO DIỆN WEB ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    # API Stream video liên tục
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_latest_text')
def get_latest_text():
    # API để JavaScript dưới web gọi lên lấy chữ cái đang nhận diện
    global latest_text
    return jsonify({"text": latest_text})

@app.route('/start_camera', methods=['POST'])
def start_camera():
    global camera
    if camera is None or not camera.isOpened():
        camera = cv2.VideoCapture(0)
    return jsonify({"status": "success"})

@app.route('/stop_camera', methods=['POST'])
def stop_camera():
    global camera
    if camera is not None:
        camera.release()
        camera = None
    return jsonify({"status": "success"})

@app.route('/save_history', methods=['POST'])
def save_history():
    # API nhận câu hoàn chỉnh và lưu vào SQLite Database
    data = request.get_json()
    content = data.get('content', '')
    if content:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO History (text_content) VALUES (?)", (content,))
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "message": "Saved"})
    return jsonify({"status": "error", "message": "Empty content"})

@app.route('/get_history')
def get_history():
    # API lấy ra 10 câu dịch gần nhất để hiển thị
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT id, text_content, datetime(created_at, 'localtime') FROM History ORDER BY id DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    history = [{"id": r[0], "content": r[1], "time": r[2]} for r in rows]
    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

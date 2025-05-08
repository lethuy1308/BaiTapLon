### 📝 **Giới thiệu**

Dự án này giúp bạn **tự động lấy tin tức từ chuyên mục AI trên trang báo VNExpress** và lưu thành **file Excel**. Mỗi ngày lúc **6 giờ sáng**, chương trình sẽ tự động chạy và cập nhật dữ liệu mới.

### 🚀 Chức năng chính

🌐 Truy cập trang báo VNExpress: Truy cập chuyên mục [AI - Công nghệ](https://vnexpress.net/cong-nghe/ai)

🧠 Lấy dữ liệu tự động:  Lấy tiêu đề, tóm tắt, nội dung và hình ảnh của bài viết

📁 Lưu dữ liệu:   Lưu tất cả thông tin vào file Excel (*.xlsx)

⏰ Tự động chạy:   Chạy hàng ngày lúc 6:00 sáng

### 🛠️ Cài đặt và chạy

#### ✅ Bước 1: Cài thư viện

Chạy lệnh sau trong terminal:

`pip install -r requirements.txt` 

#### ✅ Bước 2: Cài ChromeDriver

-   Tải ChromeDriver phù hợp: https://sites.google.com/chromium.org/driver/
    
-   Giải nén vào cùng thư mục với `main.py`, hoặc thêm vào hệ thống `PATH`.
    

----------

### ▶️ Chạy chương trình

Chạy bằng lệnh:

`python main.py` 

Chương trình sẽ tự động:

1.  Mở trình duyệt
    
2.  Duyệt các trang tin tức AI
    
3.  Lưu thông tin vào file Excel
    
4.  Lặp lại hàng ngày lúc 6:00 sáng

### 📅 Lên lịch tự động

Được thiết lập để chạy hàng ngày:

`schedule.every().day.at("06:00").do(chay)` 

Bạn không cần mở thủ công mỗi ngày – chỉ cần để máy bật.

----------

### 📦 Cấu trúc dự án

`.
├── main.py # Tập tin chính để thu thập dữ liệu
├── requirements.txt # Danh sách các thư viện cần thiết
├── README.md # Tài  liệu hướng dẫn`
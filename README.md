# Web Blog

Web Blog là một ứng dụng web blog được xây dựng bằng Django. Ứng dụng cho phép người dùng xem các bài viết, tìm kiếm, bình luận, thích bài viết và nhiều tính năng khác.

## Các tính năng chính

- **Danh sách bài viết**: Hiển thị danh sách các bài viết trên trang chính.
- **Danh mục**: Xem các bài viết phân loại theo danh mục.
- **Chi tiết bài viết**: Đọc chi tiết các bài viết.
- **Phân trang**: Điều hướng giữa các trang bài viết.
- **Bình luận**: Người dùng có thể bình luận trên bài viết.
- **Tìm kiếm**: Tìm kiếm bài viết theo từ khóa.
- **Bài viết liên quan**: Hiển thị các bài viết liên quan/suggested.
- **Lưu bài viết yêu thích**: Lưu và quản lý các bài viết yêu thích.
- **Chia sẻ trên mạng xã hội**: Chia sẻ bài viết lên các nền tảng mạng xã hội.

## Công nghệ sử dụng

- **Django**: Phiên bản 5.x
- **Bootstrap 5**: Giao diện người dùng
- **HTML, CSS, JavaScript**: Frontend
- **SQL**: Database  
- **Redis**: cache
...

## Cài đặt

1. **Clone repository**

   ```bash
   git clone https://github.com/yourusername/hieu-tv-blog.git
   
2. **Chuyển đến thư mục dự án**
    ```bash
    cd hieu-tv-blog
3. **Tạo và kích hoạt môi trường ảo**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Trên Windows: venv\Scripts\activate
4. **Cài đặt các phụ thuộc**
    ```bash
    pip install -r requirements.txt

5. **Thực hiện các migration**
    ```bash
    python manage.py migrate
6. **Khởi chạy ứng dụng**
    ```bash
    python manage.py runserver
7. **Truy cập ứng dụng tại**
    ```bash
    http://localhost:8000
8. **Truy cập admin panel**
    ```bash
    http://localhost:8000/admin

# File: gunicorn_config.py

bind = '0.0.0.0:8000'  # Chỉ định địa chỉ và cổng mà gunicorn sẽ lắng nghe
workers = 2  # Số lượng worker processes
timeout = 30  # Timeout cho mỗi request (giây)

# Đường dẫn tới module và callable function của ứng dụng
# Trong trường hợp này, module là 'app' và callable function cũng là 'app'
# Đảm bảo rằng đường dẫn tới module đúng với cấu trúc thư mục của ứng dụng của bạn
# Ví dụ: nếu ứng dụng của bạn nằm trong thư mục 'src' và có tên là 'my_app', bạn cần chỉ định 'src.my_app:app'
# Nếu module của bạn không nằm trong thư mục hiện tại, bạn cần chỉ định đường dẫn tuyệt đối.
app_module = 'apps'
callable = 'apps'

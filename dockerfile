# Sử dụng image chính thức của Python làm base image
FROM python:3

# Thiết lập thư mục làm việc trong container
WORKDIR /usr/src/app

# Sao chép các tệp requirements.txt và cài đặt các phụ thuộc
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn vào container
COPY . .

# Cấu hình biến môi trường
ENV PYTHONUNBUFFERED=1

# Mở cổng mà ứng dụng Django sẽ chạy
EXPOSE 8000

# Lệnh để chạy ứng dụng Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


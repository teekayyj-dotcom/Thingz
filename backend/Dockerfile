# Sử dụng base image Python chính thức (ví dụ: python:3.11-slim)
FROM python:3.11-slim

# Thiết lập biến môi trường
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app

# Tạo và chuyển đến thư mục làm việc
WORKDIR $APP_HOME

# Copy requirements và cài đặt dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source code
COPY . $APP_HOME

# Command chạy ứng dụng (sử dụng Gunicorn/Uvicorn để chạy production)
# Gunicorn sẽ quản lý các worker Uvicorn.
CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]

# Expose cổng
EXPOSE 8000
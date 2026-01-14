FROM python:3.13-slim

# Install system packages (Tesseract OCR)
RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run Gunicorn on the correct port for Render
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:10000"]
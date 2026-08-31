FROM python:3.11-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/install -r requirements.txt

FROM python:3.11-alpine
WORKDIR /app
COPY --from=builder /install /usr/local/lib/python3.11/site-packages
COPY app.py .
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD wget -qO- http://localhost:5000/ || exit 1
CMD ["python","app.py"]

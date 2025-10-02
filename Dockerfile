FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && pip install waitress
COPY . .
ENV PYTHONUNBUFFERED=1
EXPOSE 5001
CMD ["waitress-serve", "--host=0.0.0.0", "--port=5001", "app:app"]


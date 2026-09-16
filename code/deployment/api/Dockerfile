FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY code/deployment/api/main.py .
COPY models/model.pkl models/model.pkl

ENV MODEL_PATH=/app/models/model.pkl

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

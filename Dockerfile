# 1. Base Image
FROM python:3.10-slim

# 2. Set Working Directory
WORKDIR /app

# 3. Copy Requirements & Install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy Application Files
COPY . .

# 5. Expose Streamlit Default Port
EXPOSE 8000 8501

CMD uvicorn app.app:app --host 0.0.0.0 --port 8000 & streamlit run frontend/frontend.py --server.port=8501 --server.address=0.0.0.0

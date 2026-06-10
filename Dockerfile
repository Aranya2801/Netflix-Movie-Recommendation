FROM python:3.11-slim

LABEL maintainer="Aranya2801"
LABEL description="Netflix Movie Recommendation System — CineAI"
LABEL version="2.0.0"

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps (layered for caching)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
        numpy pandas scikit-learn scipy joblib \
        fastapi uvicorn streamlit plotly \
        sentence-transformers loguru pydantic \
        python-dotenv requests httpx

# Copy source
COPY src/ ./src/
COPY app/ ./app/
COPY scripts/ ./scripts/
COPY data/ ./data/

# Expose ports: Streamlit + FastAPI
EXPOSE 8501 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Default: run Streamlit app
CMD ["streamlit", "run", "app/streamlit_app.py", \
     "--server.port=8501", \
     "--server.address=0.0.0.0", \
     "--server.headless=true", \
     "--theme.base=dark", \
     "--theme.primaryColor=#E50914"]

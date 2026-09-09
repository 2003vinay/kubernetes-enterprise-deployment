FROM python:3.12-slim
LABEL maintainer="Vinay Malyala"
LABEL project="Enterprise CI/CD Pipeline"
LABEL version="1.2.0"
LABEL description="CI/CD Pipeline using GitHub Actions, Docker and AWS EC2"
WORKDIR /app
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
CMD curl -f http://localhost:5000/health || exit 1
CMD ["python", "-m", "apps.app"]

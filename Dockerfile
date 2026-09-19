FROM python:3.10-slim-bookworm

RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "SHUKLAMUSIC"]

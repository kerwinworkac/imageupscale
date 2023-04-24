FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y libopencv-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create a new directory /images and give all permissions
RUN chmod 777 -R /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
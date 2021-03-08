FROM python:3.7-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install python-pip build-essential cmake pkg-config libx11-dev libatlas-base-dev libgtk-3-dev libboost-python-dev -y

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "api.py"]
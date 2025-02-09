FROM python:3.8

WORKDIR /app

COPY requirements.txt ./


RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 5000

CMD nohup python -m flask --app SystemApi run --host 0.0.0.0 --port 5000

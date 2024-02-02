FROM python:3.12-alpine

WORKDIR /app

COPY . /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
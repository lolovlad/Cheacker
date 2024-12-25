FROM python:3.11
RUN apt-get -y update
RUN apt install time
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD python3 /app/main.py
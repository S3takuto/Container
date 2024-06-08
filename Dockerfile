FROM python:3.11

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \ 
    libgl1-mesa-glx \ 
    libglib2.0-0 \ 
    && rm -rf /var/lib/apt/lists

#RUN pip install gunicorn
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=application.py
ENV FLASK_ENV=production

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "application:app"]
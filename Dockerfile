FROM python:3.11

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \ 
    libgl1-mesa-glx \ 
    libglib2.0-0 \ 
    && rm -rf /var/lib/apt/lists

RUN pip install -r requirements.txt

ENV FLASK_APP=application.py
ENV FLASK_ENV=production

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
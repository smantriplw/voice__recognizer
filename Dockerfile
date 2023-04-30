FROM python:3.9

WORKDIR /usr/app
COPY . /usr/app

RUN pip install -r requirements.txt

EXPOSE 3000
CMD ['python', 'main.py']
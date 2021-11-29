FROM python:3.9-buster

WORKDIR /www

RUN python3 -m pip install -U pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY .sample.env .env
COPY . .

EXPOSE 5000

ENTRYPOINT [ "flask", "run" ]
CMD [ "--host=0.0.0.0" ]

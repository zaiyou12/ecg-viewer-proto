FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3.6 python3-pip

WORKDIR /home/back-end

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .
# COPY app app
# COPY .prod.env .env
# COPY boot.sh config.py server.py ./
# RUN chmod +x boot.sh

EXPOSE 5000
CMD ["python3", "test_booting.py"]
# ENTRYPOINT [ "./boot.sh" ]

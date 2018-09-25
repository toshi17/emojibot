FROM python:3.6

ADD . /opt
WORKDIR /opt

RUN apt-get update && apt-get install -y \
    python3-pip libgl1-mesa-dev libglu1-mesa-dev

RUN pip3 install -r requirements.txt

RUN useradd -m myuser
USER myuser

CMD python3 run.py

FROM python:3.10-alpine

# Labels
LABEL org.opencontainers.image.source https://github.com/WatcherWhale/SecProA

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./modules/ ./modules/
COPY *.py ./

CMD [ "python", "/app/checklist.py"]

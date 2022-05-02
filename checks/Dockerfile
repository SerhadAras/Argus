ARG registry
FROM $registry/checklist:template

# Labels
LABEL org.opencontainers.image.source https://github.com/WatcherWhale/SecProA

ARG checklist

WORKDIR /app/checks

RUN apk update
COPY ./$checklist/packages.txt .
RUN cat packages.txt | xargs apk --no-cache add

COPY ./$checklist/requirements.txt .
RUN pip install -r requirements.txt

COPY ./$checklist/ .

FROM python:3.9-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt update && apt upgrade -y

RUN useradd -ms /bin/bash tufin

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME ["/usr/src/app/data"]

USER root

CMD ["python", "./Final_ipv4_addr_aggr.py", "/usr/src/app/data/coalesce_input.csv"]

FROM python:3.11@sha256:380d708853b1564b71ad3744a69895d552099f618df60741c5d4a9e9e65873b9

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

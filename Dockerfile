FROM python:3.11@sha256:aed4e082c20dacc1589441112e1e9ed38b63e8e381979bfbe5c6111f04f4e227

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

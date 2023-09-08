FROM python:3.11@sha256:686efecb5c589eebe2e0feba8c163c7b96f08c6cb7fed0abc80b617d01363bb8

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

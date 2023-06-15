FROM python:3.11@sha256:2dd2f9000021839e8fba0debd8a2308c7e26f95fdfbc0c728eeb0b5b9a8c6a39

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

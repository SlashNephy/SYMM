FROM python:3.11@sha256:2d54efcc49f2e63b222ad191704c73d70c1d1fe60e114d2b100261a45c6d3a2a

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

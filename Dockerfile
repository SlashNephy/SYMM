FROM python:3.11@sha256:02808bfd640d6fd360c30abc4261ad91aacacd9494f9ba4e5dcb0b8650661cf5

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

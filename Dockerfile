FROM python:3.11@sha256:fe68f3194a1a6df058901085495abca83d8841415101366c3a4c66f06f39760a

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

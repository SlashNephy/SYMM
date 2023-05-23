FROM python:3.11@sha256:17406cbc3e7ad62ec60a706c6791e78e6a2b44e6054c02e0a31c339926cb4299

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

FROM python:3.11@sha256:8488a4b1a393b0b2cb479a2da0a0d11cf816a77c0f9278205015148adadf9edf

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

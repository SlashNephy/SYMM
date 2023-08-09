FROM python:3.11@sha256:44729cbb05832da5c0c1c6481814e71e20731933a32b3401ee510f79e8185d4b

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

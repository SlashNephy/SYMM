FROM python:3.11@sha256:e73c486856ff002ec13961c05dab8f6ff1688922895b574647a695bfc163e52f

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

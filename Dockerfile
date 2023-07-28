FROM python:3.11@sha256:2263944e52112e615353637321b137c6ea2942d0a9977434d0874b2fb605f496

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

FROM python:3.11@sha256:e7b98cbd26cbc371e0fdb039f92bb95d566b58296a26ada0fe88b3e24991fcf4

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

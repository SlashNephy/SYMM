FROM python:3.11@sha256:70f1eb2927a8ef72840254b17024d3a8aa8c3c9715a625d426a2861b5899bc62

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

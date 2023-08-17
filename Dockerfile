FROM python:3.11@sha256:85b3d192dddbc96588b719e86991e472b390805a754681a38132de1977d8e429

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

FROM python:3.11@sha256:3a619e3c96fd4c5fc5e1998fd4dcb1f1403eb90c4c6409c70d7e80b9468df7df

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

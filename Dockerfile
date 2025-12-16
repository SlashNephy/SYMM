FROM python:3.11@sha256:ddc4560e6e692d47cc5e3109ea978d4a4f7d3ccab24557dedefd278563e2b1a2

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

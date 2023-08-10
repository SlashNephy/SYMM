FROM python:3.11@sha256:bc1d76a8360d77a6ab467a8c48ce40369707c9aa76492df094968ce55cca88ae

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

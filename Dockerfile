FROM python:3.11@sha256:385990eda65578a384e44cbdccc78104be194412686b6b2af47e319bdeef0405

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

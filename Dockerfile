FROM python:3.11@sha256:ad6149f24084cc4af992bb5c1bf0171cede4f799f7dab23ab0117852ca47989d

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

COPY symm/ /app/symm/

WORKDIR /app/symm
ENTRYPOINT [ "python", "-u", "main.py" ]

FROM --platform=linux/arm64/v8 arm64v8/python:3.11-slim

LABEL org.opencontainers.image.source="https://github.com/ducky4life/factorization"

COPY requirements.txt /

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

WORKDIR /

COPY static static

COPY templates templates

COPY app.py generator.py /

EXPOSE 8080

CMD ["python", "app.py"]